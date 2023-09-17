import unittest
from my_task import Rectangle


class TestRectangle(unittest.TestCase):
    def test_calc_len(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.calc_len(), 14)

    def test_calc_square(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.calc_square(), 12)

    def test_addition(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(5, 2)
        r3 = r1 + r2
        self.assertEqual(r3.calc_len(), 16)
        self.assertEqual(r3.calc_square(), 20)

    def test_subtraction(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(2, 2)
        r3 = r1 - r2
        self.assertEqual(r3.calc_len(), 10)
        self.assertEqual(r3.calc_square(), 10)

    def test_comparison(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(2, 5)
        self.assertTrue(r1 == r1)
        self.assertTrue(r1 != r2)
        self.assertTrue(r1 < r2)
        self.assertTrue(r1 <= r2)
        self.assertTrue(r2 > r1)
        self.assertTrue(r2 >= r1)


if __name__ == '__main__':
    unittest.main(verbosity=True)
