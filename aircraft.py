import csv

class Aircraft:
	def __init__(self, aircraft_code, aircraft_type, aircraft_units, aircraft_manufacturer, aircraft_range):
		self.code = aircraft_code
		self.type = aircraft_type
		self.units = aircraft_units
		self.manufacturer = aircraft_manufacturer
		self.range = aircraft_range
		self.fuel = 100

	def set_airport(self, current_airport):
		self.airport = current_airport

	def set_fuel(self, current_fuel):
		self.fuel = current_fuel

	def get_fuel(self):
		return self.fuel

	def __str__(self):
		return "Code: {}, Type: {}, Units: {}, Manufacturer: {}, Range: {}". format (self.code
		, self.type, self.units, self.manufacturer, self.range)

class Fleet:
	aircraft_file = 'aircraft.csv'

	def __init__(self, aircraft_list = aircraft_file):
		self.fleet = self.get_aircraft(aircraft_list)
		
		
	def get_aircraft(self, aircraft_list):
		planes = []

		with open(aircraft_list, newline='') as aircrafts:
			aircraft_read = csv.DictReader(aircrafts)
			for row in aircraft_read:
				plane = Aircraft(row['code'], row['type'], row['units'], row['manufacturer'], ['range'])
				planes.append(plane)
		return planes

	def __str__(self):
		return "\n".join(map(str, self.fleet))


def main():
	myFleet = Fleet()
	print(myFleet)
		
main()