import unittest
import fibonacci

class TestCase(unittest.TestCase):
	def test_fib(self):
		result = fibonacci.fibCalc(5)
		self.assertEqual(result, 5)
             
		result = fibonacci.fibCalc(0)
		self.assertEqual(result, 0)

		result = fibonacci.fibCalc(1)
		self.assertEqual(result, 1)

		result = fibonacci.fibCalc(2)
		self.assertEqual(result, 1)

		result = fibonacci.fibCalc(10)
		self.assertEqual(result, 55)
		return

	def test_factorial(self):
		result = fibonacci.factCalc(0)
		self.assertEqual(result, 1)

		result = fibonacci.factCalc(3)
		self.assertEqual(result, 6)

		result = fibonacci.factCalc(5)
		self.assertEqual(result, 120)
		return
