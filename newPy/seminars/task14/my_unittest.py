import unittest
from task112 import clean_text


class TestCleanText(unittest.TestCase):
    def test_one_clean_text(self):
        self.assertEqual(clean_text('Some text, тест'), 'some text, ')

    def test_two_clean_text(self):
        self.assertEqual(clean_text('Hell456o worущшуd!'), 'hello word!')

    def test_three_clean_text(self):
        self.assertEqual(clean_text('У меня есть подруга Anna! Ей 21 год.'),
                         '    anna!   .', msg='Что то пошло не так ...')


if __name__ == '__main__':
    unittest.main(verbosity=2)
