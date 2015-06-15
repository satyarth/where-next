import math

class Coordinate:
	def __init__(self, vector, system='geo'):
		if system == 'geo':
			self.lat = vector[0]
			self.lon = vector[1]
			self.geo_to_spherical()
			self.spherical_to_cartesian()

		elif system == 'spherical':
			self.polar = vector[0]
			self.azimuthal = vector[1]
			self.spherical_to_cartesian()
			self.spherical_to_geo()

		elif system == 'cartesian':
			self.x = vector[0]
			self.y = vector[1]
			self.z = vector[2]
			self.cartesian_to_spherical()
			self.spherical_to_geo()

		else:
			pass

	def spherical_to_cartesian(self):
		self.x = math.sin(self.polar)*math.cos(self.azimuthal)
		self.y = math.sin(self.polar)*math.sin(self.azimuthal)
		self.z = math.cos(self.polar)

	def cartesian_to_spherical(self):
		self.polar = math.acos(self.z)
		self.azimuthal = math.atan2(self.y, self.x)

	def geo_to_spherical(self):
		self.polar = (-self.lat + 90)*math.pi/180
		self.azimuthal = self.lon*math.pi/180

	def spherical_to_geo(self):
		self.lat = -(self.polar*180/math.pi - 90)
		self.lon = self.azimuthal*180/math.pi

	def geo(self):
		return (self.lat, self.lon)
		
	def spherical(self):
		return (self.polar, self.azimuthal)
		
	def cartesian(self):
		return (self.x, self.x, self.z)

	def mod(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def normalize(self):
		mod = self.mod()
		self.x /= mod
		self.y /= mod
		self.z /= mod
		self.cartesian_to_spherical()
		self.spherical_to_geo()
		return self