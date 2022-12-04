import unittest

from exercise_2 import when_will_you_turn_onehundred as turn_hun

class TestWhenAgeIsOneHundred(unittest.TestCase):

	def test_when_will_you_turn_onehundred(self):
		""" will the age 30 show 2092? """

		test_func = turn_hun()
		answer = 'uchenna 2092'
		self.assertEqual(test_func, answer)

if __name__ == '__main__':
	unittest.main()
