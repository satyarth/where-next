import unittest
from coordinate import Coordinate

# cities = ['Abidjan', 'Manila', 'Auckland']

class TestCase(unittest.TestCase):
	def test_conversion(self):
		c = Coordinate((0, 0))
		self.assertEqual(c.cartesian(), (1, 0, 0))



if __name__ == '__main__':
    unittest.main()