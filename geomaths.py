from coordinate import Coordinate
import math

# Returns the cross product of two position vectors

def cross(a, b):
	x = a.y*b.z - a.z*b.y
	y = a.z*b.x - a.x*b.z
	z = a.x*b.y - a.y*b.x	

	return(Coordinate((x, y, z), 'cartesian'))

# Scalar product of two vectors

def dot(a, b):
	return a.x*b.x + a.y*b.y + a.z*b.z

# Distance between two given points in terms of central angle

def distance(a, b):
	return math.atan2(cross(a, b).mod(), dot(a, b))

# Returns the midpoint of two points

def midpoint(a, b):
	polar = (a.polar + b.polar)/2
	azimuthal = (a.azimuthal + b.azimuthal)/2

	return(Coordinate((polar, azimuthal), 'spherical'))

# Returns the perpendicular to the plane of the geodesic that perpendicularly bisects two points

def perpendicular_bisector(a, b):
	midpt = midpoint(a, b)
	geodesic = cross(a, b)

	return cross(midpt, geodesic)

# Returns a tuple of the two points at which the geodesics perpendicular to the given vectors intesect

def intersections(a, b):
	return (cross(a, b), cross(b, a))

# Returns a tuple of the two circumcenters of the triangle defined by the three given points

def circumcenters(a, b, c):
	return intersections(perpendicular_bisector(a, b), perpendicular_bisector(b, c))