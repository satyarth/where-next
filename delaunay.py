# Delaunay triangulation of points on a sphere using an incremental algorithm.

import geomaths

def is_delaunay(triangle, points):
	circumcenter = geomaths.circumcenter(triangle[0], triangle[1], triangle[2])
	radius = geomaths.distance(circumcenter, triangle[0])
	for point in points:
		if geomaths.distance < radius:
			return False
	return True