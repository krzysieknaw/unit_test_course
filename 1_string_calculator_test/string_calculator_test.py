import unittest
from string_calculator import string_calculator


class test_string_calculator(unittest.TestCase):
    def test_empty(self):
        actual = string_calculator("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_nr(self):
        for nr in ['0','1','12','-1','-12']:
            actual = string_calculator(nr)
            expected = int(nr)
            self.assertEqual(actual, expected)

    def test_multi_nrs(self):
       actual = string_calculator('1,2,3')
       expected = 6
       self.assertEqual(actual, expected)

    def test_int_input(self): #  to fail
       actual = string_calculator(1,2)
       expected = 3
       self.assertEqual(actual, expected)

    def test_non_numeric_input(self): #  to fail
       actual = string_calculator('a,b,c')
       expected = "what should I expect?"
       self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
