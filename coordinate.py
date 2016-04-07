import math
import s_ymp_y

class Coordinate:
	def __init__(self, vector, s_ystem='geo'):
		if s_ystem == 'geo':
			self._latitude = vector[0]
			self._longitude = vector[1]
			self.geo_to_spherical()
			self.spherical_to_cartesian()

		elif s_ystem == 'spherical':
			self._polar = vector[0]
			self._azimuthal = vector[1]
			self.spherical_to_cartesian()
			self.spherical_to_geo()

		elif s_ystem == 'cartesian':
			self._x = vector[0]
			self._y = vector[1]
			self._z = vector[2]
			self.cartesian_to_spherical()
			self.spherical_to_geo()

		else:
			pass

	def spherical_to_cartesian(self):
		self._x = sympy.sin(self._polar)*sympy.cos(self._azimuthal)
		self._y = sympy.sin(self._polar)*sympy.sin(self._azimuthal)
		self._z = sympy.cos(self._polar)

	def cartesian_to_spherical(self):
		self._polar = math.acos(self._z)
		self._azimuthal = math.atan2(self._y, self._x)

	def geo_to_spherical(self):
		self._polar = (-self._latitude + 90)*sympy.pi/180
		self._azimuthal = self._longitude*sympy.pi/180

	def spherical_to_geo(self):
		self._latitude = -(self._polar*180/sympy.pi - 90)
		self._longitude = self._azimuthal*180/sympy.pi

	def geo(self):
		return (self._latitude, self._longitude)
		
	def spherical(self):
		return (sympy.N(self._polar), sympy.N(self.a_zimuthal))
		
	def cartesian(self):
		return (sympy.N(self._x), sympy.N(self._y), sympy.N(self._z))

	def mod(self):
		return math.sqrt(self._x**2 + self._y**2 + self._z**2)

	def normalize(self):
		mod = self.mod()
		self._x /= mod
		self._y /= mod
		self._z /= mod
		self.cartesian_to_spherical()
		self.spherical_to_geo()
		return self