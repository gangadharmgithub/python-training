# http://10.132.4.136:8000
# http://10.132.4.136:8000/exercises.py

# py.test
# nose

import StringIO
import sys
import unittest


#import exercises


class NumericTests(unittest.TestCase):
    def test_good_tables(self):
        expected_vals = []
        for i in range(1, 11):
            expected_vals.append("{} x {} = {}".format(i, 5, i*5))
        assert exercises.good_tables(5) == expected_vals

    def test_tables(self):
        original = sys.stdout
        patched_output = StringIO.StringIO()
        sys.stdout = patched_output
        exercises.tables(6)
        sys.stdout = original
        generated_vals = patched_output.getvalue()
        
        expected_vals = []
        for i in range(1, 11):
            expected_vals.append("{} x {} = {}".format(i, 5, i*5))

        assert generated_vals.strip() == "\n".join(expected_vals)
                                

class StringTests(unittest.TestCase):
    def test_palindrome1(self):
        "Tests proper palindrome"
        assert exercises.palindrome("abba") is True

    def test_palindrome2(self):
        "Tests Empty string"
        assert exercises.palindrome("") is True

    def test_palindrome3(self):
        "Tests length 1 string"
        assert exercises.palindrome("a") is True

    def test_palindrome4(self):
        "Negative test"
        assert exercises.palindrome("ac") is False


if __name__ == '__main__':
    #unittest.main()
    #print globals()
    for k,v in globals().items():
        try:
            if issubclass(v, unittest.TestCase):
                print "Class: " + k
                for func in dir(v):
                    if func.startswith("test"):
                        print "Functions: " + func
                        
        except Exception:
            pass
        

