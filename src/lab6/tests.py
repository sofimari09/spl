import unittest
from src.lab1.calculator_operations import *
from src.lab1.console_interaction import *

class TestCalculatorOperations(unittest.TestCase):

    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

        result = add(-2, 3)
        self.assertEqual(result, 1)

        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_subtraction(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

        result = subtract(-2, 3)
        self.assertEqual(result, -5)

        result = subtract(-2, -3)
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

        result = multiply(-2, 3)
        self.assertEqual(result, -6)

        result = multiply(-2, -3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

        result = divide(-6, 3)
        self.assertEqual(result, -2)

        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)

    def test_error_handling(self):
        with self.assertRaises(ArithmeticError):
            compute_square_root(-4)

        with self.assertRaises(ArithmeticError):
            change_decimal_places(0)

if __name__ == '__main__':
    unittest.main()
