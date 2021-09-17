import unittest
from kata import Add

class StringCalcTests(unittest.TestCase):
    
    # Step 1 tests
    def test_empty_string(self):
        test_string = ''
        test_sum = 0
        self.assertEqual(Add(test_string), test_sum)

    def test_two_nums(self):
        test_string = '2,4'
        test_sum = 2+4
        self.assertEqual(Add(test_string), test_sum)

    # Step 2 tests
    def test_four_nums(self):
        test_string = '4,8,1,9'
        test_sum = 4+8+1+9
        self.assertEqual(Add(test_string), test_sum)

    def test_ten_nums(self):
        test_string = '1,6,1,8,3,2,12,56,4,87'
        test_sum = 1+6+1+8+3+2+12+56+4+87
        self.assertEqual(Add(test_string), test_sum)

    # Step 3 tests
    def test_new_line(self):
        test_string = '1\n3'
        test_sum = 1+3
        self.assertEqual(Add(test_string), test_sum)

    def test_new_line_comma(self):
        test_string = '1\n3,5'
        test_sum = 1+3+5
        self.assertEqual(Add(test_string), test_sum)

    # Step 4 tests
    def test_custom_delimiters(self):
        test_string = '//&\n4&9'
        test_sum = 4+9
        self.assertEqual(Add(test_string), test_sum)

    def test_multiple_character_delimiter(self):
        test_string = '//howdy\n1howdy4'
        test_sum = 1+4
        self.assertEqual(Add(test_string), test_sum)

    def test_multiple_character_delimiter_no_nums(self):
        test_string = '//howdy\n'
        test_sum = 0
        self.assertEqual(Add(test_string), test_sum)

    def test_new_line_custom_delimiter(self):
        test_string = '//\n\n4\n3'
        test_sum = 4+3
        self.assertEqual(Add(test_string), test_sum)

    def test_new_line_no_nums(self):
        test_string = '//\n\n'
        test_sum = 0 
        self.assertEqual(Add(test_string), test_sum)

    # Step 5 tests
    def test_single_negative(self):
        with self.assertRaises(Exception) as context:
            Add('-2')
        self.assertTrue(context.exception, 'Negatives not allowed: [-2]')

    def test_negative_positive_mix(self):
        with self.assertRaises(Exception) as context:
            Add('-2,-5,10')
        self.assertTrue(context.exception, 'Negatives not allowed: [-2, -5]')

    def test_negatives_only(self):
        with self.assertRaises(Exception) as context:
            Add('-4,-3')
        self.assertTrue(context.exception, 'Negatives not allowed: [-4, -3]')

if __name__ == '__main__':
    unittest.main()