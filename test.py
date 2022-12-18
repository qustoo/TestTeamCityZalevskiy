from main import Factorial
import unittest

class TestMyFactoral(unittest.TestCase):
    def test_negative_number(self):
        res = Factorial(-1)
        self.assertEqual(res,None)

    def test_big_negative_numver(self):
        res = Factorial(-10000)
        self.assertEqual(res,None)

    def test_positive_small_number(self):
        res = Factorial(5)
        self.assertEqual(res,120)

    def test_positive_big_number(self):
        res = Factorial(20)
        self.assertEqual(res,2432902008176640000)

    def test_incorrect_input(self):
        res = Factorial("hahaha")
        print(res)
        self.assertEqual(res,None)


