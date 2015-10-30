#!/usr/bin/env python

import cmd
import json
import logging
import sys

import requests

logging.basicConfig(level = logging.CRITICAL)

API_KEY = "c17e866d23444d07854392dc18b911e3"


class OSClient(cmd.Cmd):
    """Simple command line tool to manipulate Openstack 
    compute API"""
    def __init__(self):
        self.tenant_id = self.session_token = None
        self.images = []
        self.flavours = []
        cmd.Cmd.__init__(self)
        
    def error(self, message):
        print "ERROR : {}".format(message)

    def do_hello(self, line):
        "Just says hi"
        print "Hi ", line

    def do_EOF(self, line):
        print "Thank you!"
        sys.exit(0)

    def do_images(self, line):
        "List available images"
        if not self.tenant_id or not self.session_token:
            self.error("You need to authenticate before listing images")
        else:
            if not self.images:
                list_url = "https://dfw.servers.api.rackspacecloud.com/v2/{}/images/detail".format(self.tenant_id)
                headers = {'X-Auth-Token' : self.session_token}
                resp = requests.get(list_url, headers = headers)
                resp_data = resp.json()
                self.images = resp_data['images']

            for image in self.images:
                print image['id'], image['name']

    def do_flavours(self, line):
        "List available flavours"
        if not self.tenant_id or not self.session_token:
            self.error("You need to authenticate before listing images")
        else:
            if not self.flavours:
                list_url = "https://dfw.servers.api.rackspacecloud.com/v2/{}/flavors".format(self.tenant_id)
                headers = {'X-Auth-Token' : self.session_token}
                resp = requests.get(list_url, headers = headers)
                resp_data = resp.json()
                self.flavours = resp_data['flavors']

            for flavour in self.flavours:
                print flavour['id'], flavour['name']

    
    def do_authenticate(self, line):
        auth_url = "https://identity.api.rackspacecloud.com/v2.0/tokens"
        headers = {"Content-Type":"application/json"}
        data = json.dumps(dict(auth = {"RAX-KSKEY:apiKeyCredentials" : dict(username = "nibrahim",
                                                                 apiKey = API_KEY)}))
        resp = requests.post(auth_url, headers = headers, data = data)
        resp_data = resp.json()
        session_token = resp_data['access']['token']['id']
        tenant_id = resp_data['access']['token']['tenant']['id']
        logging.debug("Obtained session token %s and tenant id %s", session_token, tenant_id)
        self.session_token =  session_token
        self.tenant_id = tenant_id
        print "Successfully authenticated"
        
    def do_create(self, line):
        "Create image_id flavour_id"
        try:
            image_id, flavour_id = line.split()
            create_server(self.session_token, 
                          self.tenant_id,
                          image_id, 
                          flavour_id)
            print "Done!"
        except ValueError:
            self.error("Malformed command")
        
        
    

def create_server(session_token, tenant_id, image_id, flavour_id):
    url = "https://dfw.servers.api.rackspacecloud.com/v2/{}/servers".format(tenant_id)
    headers = {"X-Auth-Token" : session_token,
               "Content-Type": "application/json",
               "X-Auth-Project-Id": "training project"}
    data = json.dumps({
        "server" : {
            "name" : "Virident test server",
            "imageRef" : image_id,
            "flavorRef" : flavour_id,
            "metadata" : {
                "My Server Name" : "Ubuntu 11.10 server"
            }
        }
    })
    resp = requests.post(url, headers = headers, data = data)
    


def main2():
    interpreter = OSClient()
    interpreter.cmdloop()
    
if __name__ == '__main__':
    main2()
    




# server = RackspaceServer("http://sdsdasdsa")

# server.connect(api_key)
# for i in server.images:
# for i in server.flavours:
    
# server.create()
