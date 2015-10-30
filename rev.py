

import sys

def reverse_lines(fname):
    with open(fname) as f:
        for i in f:
            print i.strip()[::-1]

if __name__ == '__main__':
    reverse_lines(sys.argv[1])
