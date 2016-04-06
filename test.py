from coordinate import Coordinate
from geomaths import *
from pygeocoder import Geocoder
from pygeolib import GeocoderError

cities = ['Abidjan', 'Manila', 'Auckland']
coordinates = []


for city in cities:
	print(Geocoder.geocode(city).coordinates)
	coordinates.append(Coordinate(Geocoder.geocode(city).coordinates))


cc = circumcenter(coordinates[0],coordinates[1],coordinates[2])

print(cc.geo(), antipode(cc).geo())
print(distance(coordinates[0], cc), distance(coordinates[0], antipode(cc)))
print(Geocoder.reverse_geocode(cc.geo()[0], cc.geo()[1]))

# a = Coordinate((48.24,7.73))
# b = Coordinate((66.38, 78))
# c = Coordinate((30.5, 97.7))

# cc = circumcenter(a,b,c)
# print cc.geo(), antipode(cc).geo()
# print distance(b, cc), distance(a, antipode(cc))