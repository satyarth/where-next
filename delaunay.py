# Delaunay triangulation of points on a sphere using an incremental algorithm.

import geomaths

def is_delaunay(triangle, points):
	circumcenter = geomaths.circumcenter(triangle[0], triangle[1], triangle[2])
	radius = geomaths.distance(circumcenter, triangle[0])
	for point in points:
		if geomaths.distance < radius:
			return False
	return True

# At the end of every iteration, the Delaunay condition must hold true.

def delaunay(points):
	# Triangulation starts out empty, fill it up with lists of vertices that make up the delaunay triangulation.
	triangulation = []
	# Todo:
	# Keep track of all the triangles
	# Determine which triangle a point is being inserted into
	# Find all neighbors of a selected triangle
	# Flip diagonal edge of a quadrilateral
	while points:
		pass
