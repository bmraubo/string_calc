import unittest
from kata import Add

class StringCalcTests(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(Add(''), 0)

    def test_two_nums(self):
        self.assertEqual(Add('2,4'), 6)

if __name__ == '__main__':
    unittest.main()