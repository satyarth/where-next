from coordinate import Coordinate
from geomaths import *

a = Coordinate((45, 0))
b = Coordinate((-45, 0))
c = Coordinate((0, 90))

print(circumcenters(a,c,b)[0].geo())
print(distance(a,b))