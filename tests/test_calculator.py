import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # 3 cases
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        # 3 cases
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_divide(self):
        # 3 cases (incl. divide-by-zero)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-4, 2), -2)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
