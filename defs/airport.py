class Airport(object):
	def __init__(self, airport_code, airport_name, airport_city, airport_country, airlat, airlong):
		self.code = airport_code
		self.name = airport_name
		self.country = airport_country
		self.city = airport_city
		self.lat = airlat
		self.long = airlong

	def __str__(self):
		airportstr = ""
		return "{} (Name:  {}, {}, {}, lat :{}, lon :{}) ". format (self.code
		, self.name, self.city, self.country, self.lat, self.long)