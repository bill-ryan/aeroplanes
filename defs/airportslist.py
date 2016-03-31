import csv, math

from currencies import Currencies

class AirportInfo:

	airport_file = 'airport.csv'
	country_currency_file = 'country_currency_file'

	currency_list = Currencies()
	country_currencies = currency_list.currency_countries

	def __init__(self, airport_list = airport_file):
		self.Airports = self.get_lat_long(airport_list)

	def get_lat_long(self, airport_list, currency_of_country = country_currencies):
		code_lat_long = {}
		with open(airport_list, newline='') as f:
			airport_read = csv.reader(f, delimiter=',')
			for row in airport_read:
				country = row[3]
				try:
					currency = currency_of_country[country]
				except KeyError:
					currency = 'US Dollar'
				code_lat_long[row[0]] = (row[-6], row[-5], currency)
		return code_lat_long

	def get_distances(self, air1, air2):
		lat1 = float(self.Airports[air1][0])
		long1 = float(self.Airports[air1][1])

		lat2 = float(self.Airports[air2][0])
		long2 = float(self.Airports[air2][1])

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
	
		distance = int(math.acos(math.sin(latangle1) * math.sin(latangle2) * math.cos(longangle1 - longangle2)
		+ math.cos(latangle1) * math.cos(latangle2)) * 6371)

		return distance

if "__name__" == "__main__":
	airport_list = AirportInfo()
	print(airport_list.Airports)
	print(airport_list.get_distances('2048', '2049'))