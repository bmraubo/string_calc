import unittest
from kata import Add

class StringCalcTests(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(Add(''), 0)

    def test_two_nums(self):
        self.assertEqual(Add('2,4'), 6)

    def test_4_nums(self):
        self.assertEqual(Add('4,8,1,9'), 22)

    def test_10_nums(self):
        self.assertEqual(Add('1,6,1,8,3,2,12,56,4,87'), 180)

if __name__ == '__main__':
    unittest.main()