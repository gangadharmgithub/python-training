#!/usr/bin/env python
"""
A poor mans implementation of ls. 

Supports (for some definition of the term) the -l option.

List of bugs
1. fix formatting for short listing
2. Treatment of directories in input arguments
3. 

"""

import argparse
import datetime
import glob
import grp
import logging
import os
import pwd
import stat
import sys

logging.basicConfig(level = logging.CRITICAL)

def get_filenames(d):
    """
    Returns filenames in directory d
    
    If d is None:
     then return all files in current directory
  
    if d is a list of things
     then don't expand. Just return them.

    """
    if not d:
        return glob.iglob("*")
    else:
        return d

def short_output(file_list):
    for i in file_list:
        print "{}    ".format(i),

def create_links(info):
    return info.st_nlink

def create_owner(info):
    return pwd.getpwuid(info.st_uid).pw_name

def create_group(info):
    g = grp.getgrgid(info.st_gid)
    return g.gr_name

def create_size(info):
    return info.st_size
    
def create_atime(info):
    d = datetime.datetime.fromtimestamp(info.st_atime)
    return d.strftime("%b %d %H:%M")

def create_permstring(info):
    def format_string(mask, c):
        if info.st_mode & mask:
            return c
        else:
            return '-'

    return "-{}{}{}{}{}{}{}{}{}".format(format_string(stat.S_IRUSR, "r"),
                                        format_string(stat.S_IWUSR, "w"),
                                        format_string(stat.S_IXUSR, "x"),
                                        format_string(stat.S_IRGRP, "r"),
                                        format_string(stat.S_IWGRP, "w"),
                                        format_string(stat.S_IXGRP, "x"),
                                        format_string(stat.S_IROTH, "r"),
                                        format_string(stat.S_IWOTH, "w"),
                                        format_string(stat.S_IXOTH, "x"))

    

def create_long_line(f):
    info = os.stat(f)
    return "{} {} {} {} {:5} {} {}".format(create_permstring(info),
                                           create_links(info),
                                           create_owner(info),
                                           create_group(info),
                                           create_size(info),
                                           create_atime(info),
                                           f)

def long_output(file_list):
    logging.debug("Trying to print long format")
    for f in file_list:
        print create_long_line(f)


def parse_args(args):
    parser = argparse.ArgumentParser(description = "List information about the FILEs")
    parser.add_argument("-l", "--long", help = "Long format output", action = "store_true")
    parser.add_argument("-v", "--verbose", help = "Turns on debugging", action = "store_true")
    parser.add_argument("files", nargs = argparse.REMAINDER)
    args  = parser.parse_args()
    return args

def main():
    args = parse_args(sys.argv[1:])
    if args.verbose:
        logging.root.setLevel(logging.DEBUG)
    logging.debug("Long is set to {}".format(args.long))
    logging.debug("Files is set to {}".format(args.files))
    filenames = get_filenames(args.files)
    if args.long:
        long_output(filenames)
    else:
        short_output(filenames)

if __name__ == '__main__':
    main()




    
