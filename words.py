import sys

def count_words(fname):
    """ Returns number of words in file fname"""
    with open(fname) as f:
        contents = f.read()
    return len(contents.split())


if __name__ == '__main__':
    filename = sys.argv[1]
    print count_words(filename)

