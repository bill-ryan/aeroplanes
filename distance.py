import math
from destinations import Destinations

class Distance():
	def __init__(self, air1, air2):
		pass

	def dist_calc(lat1, long1, lat2, long2):
		if lat1 >= 0:
			latangle1 = 90 - lat1
		else:
			latangle1 = 90 + lat1
		if lat2 >= 0:
			latangle2 = 90 - lat2
		else:
			latangle2 = 90 + lat2
		latangle1 = math.radians(latangle1)
		latangle2 = math.radians(latangle2)
		longangle1 = math.radians(long1)
		longangle2 = math.radians(long2)
	
		d = int(math.acos(math.sin(latangle1) * math.sin(latangle2) * math.cos(longangle1 - longangle2)
		+ math.cos(latangle1) * math.cos(latangle2)) * 6371)
		return d
	
	def get_airport_distance(code1, code2):
		for i in airports:
			if code1 == i[0]:
				ap1lat = i[3]
				ap1long = i[4]
			elif code2 == i[0]:
				ap2lat = i[3]
				ap2long = i[4]
		return dist_calc(ap1lat, ap1long, ap2lat, ap2long)
