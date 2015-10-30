"""
Module to create visiting cards for people
from data read in from a csv file.
"""

import csv
import urllib


def generate_vcard(fname, lname, title, phone, email):
    vcard_template = '''BEGIN:VCARD
VERSION:2.1
N:{1};{0}
FN:{0} {1}
ORG:Raisins R Us, Inc.
TITLE:{2}
TEL;WORK;VOICE:{3}
ADR;WORK:;;100 Flat Grape Dr.;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:{4}
REV:20150922T195243Z
END:VCARD
'''
    return vcard_template.format(fname, lname, title, phone, email)

def generate_qr(data):
    root_url = 'https://chart.googleapis.com/chart?'
    params = dict(cht = "qr", chs = "300x300", chl = data)
    url = root_url + urllib.urlencode(params)
    u = urllib.urlopen(url)
    return u.read()
    
def write_vcard(vcard_data, qr_data, fname, lname):
    vcard_filename = "{}_{}.vcf".format(fname, lname)
    qr_filename = "{}_{}.png".format(fname, lname)
    with open(vcard_filename, "w") as f:
        f.write(vcard_data)
    with open(qr_filename, "w") as f:
        f.write(qr_data)
    
def parse_csv(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            lname, fname, title, email, phone = row
            print "Generating card for {} {}".format(fname, lname)
            vcard = generate_vcard(fname, lname, title, phone, email)
            qr = generate_qr(vcard)
            write_vcard(vcard, qr, fname, lname)

            
if __name__ == '__main__':
    parse_csv("raisin_team.csv")

