import unittest
from tests.hw_5_1_10 import (code_two_list,
                             code_str,
                             three,
                             add_digits,
                             zero_end,
                             arithmetic_progression,
                             unique_num,
                             missing,
                             count,
                             reverse_string)

class MyTestCase(unittest.TestCase):

    def test_code_two_list(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_result = list(set(a).intersection(b))
        self.assertEqual(code_two_list(a,b), expected_result)

    def test_code_str(self):
        self.assertEqual(code_str(), 5)

    def test_three(self):
        self.assertTrue(three(9), True)

    def test_add_digits(self):
        self.assertEqual(add_digits(48), 3)

    def test_zero_end(self):
        l =[0,2,3,4,6,7,10]
        l_compare = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(zero_end(l),l_compare)

    def test_arithmetic_progression(self):
        a = [5,7,9,11]
        self.assertTrue(arithmetic_progression(a), True)

    def test_unique_num(self):
        numbers = [5, 3, 4, 3, 4]
        self.assertEqual(unique_num(numbers), 5)

    def test_missing(self):
        numbers = [1,2,3,4,6,7,8]
        self.assertEqual(missing(numbers), 5)

    def test_count(self):
        numbers = [1,2,3,(1,2),3]
        self.assertEqual(count(numbers),3)

    def test_reverse_string(self):
        sentence = "Hello World and Coders"
        self.assertEqual(reverse_string(sentence), 'sredoC dna dlroW olleH')



if __name__ == '__main__':
    unittest.main()
