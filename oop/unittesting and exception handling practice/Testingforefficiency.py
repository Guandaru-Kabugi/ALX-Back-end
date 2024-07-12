import unittest

from simple_calculator import SimpleCalculator


class TestCalc (unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(2,3), -1)
        self.assertEqual(self.calculator.subtract(3,2), 1)
        self.assertEqual(self.calculator.subtract(-2,3), -5)
        self.assertEqual(self.calculator.subtract(-2,-3), 1)
        self.assertEqual(self.calculator.subtract(2,-3), 5)
    def test_addition(self):
        self.assertEqual(self.calculator.add(3,3), 6)
        self.assertEqual(self.calculator.add(-3,-3), -6)
        self.assertEqual(self.calculator.add(-3,3), 0)
        self.assertEqual(self.calculator.add(4,-3), 1)
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(3,3), 9)
        self.assertEqual(self.calculator.multiply(3,-3), -9)
        self.assertEqual(self.calculator.multiply(-2,3), -6)
        self.assertEqual(self.calculator.multiply(-3,-2), 6)
    def test_division(self):
        self.assertEqual(self.calculator.divide(3,3), 1)
        self.assertEqual(self.calculator.divide(6,3), 2)
        self.assertEqual(self.calculator.divide(-6,3), -2)
        self.assertEqual(self.calculator.divide(8,-2), -4)
        self.assertEqual(self.calculator.divide(0,3), None)
        self.assertEqual(self.calculator.divide(3,0), None)

if __name__ == "__main__":
    unittest.main()
