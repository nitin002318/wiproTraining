import unittest
from source.calculations import *
class Test_Calculations(unittest.TestCase):

    def test_add(self):
        res=add(10,5)
        self.assertEqual(res,15,msg="Addition Error" )

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(res, 5, msg="Addition Error")

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(res, 50, msg="Addition Error")

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(res, 2.0, msg="Addition Error")
        
    @unittest.skip(reason="Not important")
    def test_ne(self):
        res=ne(2,2)
        self.assertTrue(res,msg="test failed")
