from rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(length_cm=2)
        self.r2 = Rectangle(length_cm=2, width_cm=4)
        self.r3 = Rectangle(length_cm=2)

    def test_step_1(self):
        self.assertEqual(self.r1, self.r3)

    def test_step_2(self):
        self.assertTrue(self.r1 == self.r3, 'Сравнение рабоет не корректно')


if __name__ == '__main__':
    unittest.main()