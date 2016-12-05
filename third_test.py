import unittest
from third import count_letter_in_string

class TestThird(unittest.TestCase):

    def test_if_not_string_return_zero(self):
        self.assertEqual(count_letter_in_string(5, "a"), 0)

    def test_if_empty_string_return_zero(self):
        self.assertEqual(count_letter_in_string("", "a"), 0)

    def test_if_letter_not_in_string_return_zero(self):
        self.assertEqual(count_letter_in_string("apple", "m"), 0)

    def test_if_letter_is_in_string_return_count(self):
        self.assertEqual(count_letter_in_string("apple", "p"), 2)

if __name__ == '__main__':
    unittest.main()
