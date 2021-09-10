import unittest
from kata import Add

class StringCalcTests(unittest.TestCase):
    
    #Step 1 tests
    def test_empty_string(self):
        self.assertEqual(Add(''), 0)

    def test_two_nums(self):
        self.assertEqual(Add('2,4'), 6)

    #Step 2 tests
    def test_4_nums(self):
        self.assertEqual(Add('4,8,1,9'), 22)

    def test_10_nums(self):
        self.assertEqual(Add('1,6,1,8,3,2,12,56,4,87'), 180)

    #Step 3 tests
    def test_new_line(self):
        self.assertEqual(Add('1\n3'), 4)

    def test_new_line_comma(self):
        self.assertEqual(Add('1\n3,5'), 9)

    #Step 4 tests
    def test_other_delimiters(self):
        self.assertEqual(Add('//&\n4&9'), 13)

    def test_howdy_delimiter(self):
        self.assertEqual(Add('//howdy\n1howdy4'), 5)

    def test_howdy_no_nums(self):
        self.assertEqual(Add('//howdy\n'), 0)

    def test_new_line_custom_delimiter(self):
        self.assertEqual(Add('//\n\n4\n3'), 7)

    def test_new_line_no_nums(self):
        self.assertEqual(Add('//\n\n'), 0)

if __name__ == '__main__':
    unittest.main()