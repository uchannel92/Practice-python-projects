import unittest

from exercise_2 import is_odd_or_even as ioe
from exercise_2 import is_odd_or_even_dbl_input

class TestIsOddOrEven(unittest.TestCase):
	""" Testing the exercise_2.py file """

	def test_is_number_even(self):
		""" is number 22 even? """

		test_function = ioe(22)
		self.assertEqual(test_function, 'even')

	def test_is_twenty_two_even(self):
		""" is 3044 divisible by four? """

		test_function = ioe(3044)
		self.assertEqual(test_function, 'divisible by four, and also even')

	def test_is_number_odd(self):
		""" is number 563 odd? """

		test_function = ioe(563)
		self.assertEqual(test_function, 'odd')


	def test_even_dbl_input(self):
		""" will both values return an even val"""

		test_function = is_odd_or_even_dbl_input(16, 4)
		self.assertEqual(test_function, 'even')


if __name__ == '__main__':
		unittest.main()