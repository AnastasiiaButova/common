import unittest
from tests.homework_5 import (code_two_list,
                              code_str,
                              three,
                              add_digits)

class MyTestCase(unittest.TestCase):

    def test_code_two_list(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        actual_result = code_two_list(a,b)
        expected_result = list(set(a).intersection(b))
        self.assertEqual(expected_result, actual_result)

    def test_code_str(self):
        actual_result = code_str()
        expected_result = 5
        self.assertEqual(expected_result, actual_result)

    def test_three(self):
        actual_result = three()
        expected_result = True
        self.assertTrue(expected_result, actual_result)

    def test_add_digits(self):
        actual_result = add_digits()
        expected_result = 3
        self.assertEqual(expected_result, actual_result)







if __name__ == '__main__':
    unittest.main()
