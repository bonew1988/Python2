import unittest
from task_new import FatorialGenerator


class TestFatorialGenerator(unittest.TestCase):

    def test_default_constructor(self):
        gen = FatorialGenerator(5)
        result = list(gen)
        self.assertEqual(result, [1, 2, 6, 24, 120])

    def test_start_stop_constructor(self):
        gen = FatorialGenerator(2, 4)
        result = list(gen)
        self.assertEqual(result, [2, 6])

    def test_step_constructor(self):
        gen = FatorialGenerator(1, 5, 2)
        result = list(gen)
        self.assertEqual(result, [1, 6, 120])

    def test_empty_generator(self):
        gen = FatorialGenerator()
        result = list(gen)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
