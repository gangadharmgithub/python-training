"""
A poor man's implementation of ls

Support ls -l options

"""
import glob
import sys

def getfilenames(d):
    ''' Retruns list of files in a directory '''
    if not d:
        return glob.iglob("*")
    else:
        print("Going into else")
        return d


def output(file_list):
    for i in file_list:
        print "{}   ".format(i)
        


def main():
    args = sys.argv[1:]
    filenames = getfilenames(sys.argv[1:])
    output(filenames)
    pass

if __name__ == '__main__':
    main()
