import csv, math

from currencies import Currencies

class Airport():
	def __init__(self, airport_code, airport_name, airport_city, airport_country, airlat, airlong, curr):
		self.code = airport_code
		self.name = airport_name
		self.country = airport_country
		self.city = airport_city
		self.lat = airlat
		self.long = airlong
		self.currency = curr

	def __str__(self):
		airportstr = ""
		return "{} (Name:  {}, {}, {}, lat :{}, lon :{}) ". format (self.code
		, self.name, self.city, self.country, self.lat, self.long)

class AirportInfo:

	airport_file = 'airport.csv'
	country_currency_file = 'country_currency.csv'

	currency_list = Currencies()
	country_currencies = currency_list.currency_countries

	def __init__(self, airport_list = airport_file):
		self._airport_info = self.get_airport_info()
		self.airports = self.build_airports()

	def build_airports(self):
		airports = []
		for airport in self._airport_info:
			airport = Airport(airport, self._airport_info[airport][0], self._airport_info[airport][1], self._airport_info[airport][2],\
			self._airport_info[airport][3], self._airport_info[airport][4], self._airport_info[airport][5])
			airports.append(airport)
		return airports

	def get_airport_info(self, airport_list = airport_file, currency_of_country = country_currencies):
		airport_dict = {}
		with open(airport_list, newline='') as f:
			airport_read = csv.reader(f, delimiter=',')
			for row in airport_read:
				country = row[3]
				try: #One country (East Timor) has no currency listed, so using USD as default
					currency = currency_of_country[country]
				except KeyError:
					currency = 'US Dollar'
				airport_dict[row[0]] = (row[1], row[2], row[3], row[-6], row[-5], currency)
		return airport_dict

x = AirportInfo()
print(x)