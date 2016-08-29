from coordinate import Coordinate
import math

# Returns the antipose of a point

def antipode(a):
	lat = -a.lat
	if a.lon < 0:
		lon = a.lon + 180
	else:
		lon = a.lon - 180
	return Coordinate((lat, lon))

# Normalizes a vector

# def norm(a):
# 	x = a.x
# 	y = a.y
# 	z = a.z
# 	norm_factor = a.mod()
# 	x /= norm_factor
# 	y /= norm_factor
# 	z /= norm_factor
# 	return Coordinate((x, y, z), 'cartesian')

# Returns the cross product of two position vectors

def cross(a, b):
	x = a._y*b._z - a._z*b._y
	y = a._z*b._x - a._x*b._z
	z = a._x*b._y - a._y*b._x	

	return(Coordinate((x, y, z), 'cartesian'))

# Scalar product of two vectors

def dot(a, b):
	return a.x*b.x + a.y*b.y + a.z*b.z

# Distance between two given points in terms of central angle

def distance(a, b):
	return math.atan2(cross(a, b).mod(), dot(a, b))

# Returns the midpoint of two points

def midpoint(a, b):
	polar = (a._polar + b._polar)/2
	azimuthal = (a._azimuthal + b._azimuthal)/2

	return(Coordinate((polar, azimuthal), 'spherical'))

# Returns the perpendicular to the plane of the geodesic that perpendicularly bisects two points

def perpendicular_bisector(a, b):
	midpt = midpoint(a, b)
	geodesic = cross(a, b).normalize()

	return cross(midpt, geodesic).normalize()

# Returns a tuple of the two points at which the geodesics perpendicular to the given vectors intesect

def intersections(a, b):
	return (cross(a, b).normalize(), cross(b, a).normalize())

# Returns a tuple of the two circumcenters of the triangle defined by the three given points

def circumcenters(a, b, c):
	return intersections(perpendicular_bisector(a, b), perpendicular_bisector(b, c))

def circumcenter(a, b, c):
	return min(circumcenters(a, b, c), key=lambda point: distance(point, a))

def furthest(points, origin):
	return max(points, key = lambda point: distance(point, origin))

def closest(points, origin):
	return min(points, key = lambda point: distance(point, origin))
