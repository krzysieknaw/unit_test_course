import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_empty(self):
        actual = add("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_nr(self):
        for nr in ['0', '1', '12', '-1', '-12']:
            actual = add(nr)
            expected = int(nr)
            self.assertEqual(actual, expected)

    def test_multi_nrs(self):
        actual = add('1,2,3')
        expected = 6
        self.assertEqual(actual, expected)

    def test_multi_nrs_not_int(self): # to fail
        actual = add('1.1,2.2,3.3')
        expected = 6.6
        self.assertEqual(actual, expected)

    def test_int_input(self):  # to fail - user input is str
        actual = add(1)
        expected = 3
        self.assertEqual(actual, expected)

    def test_non_numeric_input(self):
        actual = add('a,b,c')
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
