import unittest

from exercise_2 import when_will_you_turn_onehundred as turn_hun

class TestWhenAgeIsOneHundred(unittest.TestCase):

	def test_when_will_you_turn_onehundred(self):
		""" will the age 30 show 2092? """

		test_answer = turn_hun()
		self.assertEqual(test_answer, 2092)

if __name__ == '__main__':
	unittest.main()
