import unittest

from src.calculations import add, sub, mul, div

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15, res, msg="Addition error")

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5, res, msg="Substraction error")

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50, res, msg="Multiplaction error")

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2.0, res, msg="Division error")