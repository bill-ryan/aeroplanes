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

	def __str__(self):
		return "Code: {}, Type: {}, Units: {}, Manufacturer: {}, Range: {}". format (self.code
		, self.type, self.units, self.manufacturer, self.range)

class Fleet:
	aircraft_file = 'aircraft.csv'

	def __init__(self, aircraft_list = aircraft_file):
		self.fleet_info = self.get_aircraft(aircraft_list)
		self.fleet = self.build_fleet()
		
	def get_aircraft(self, aircraft_list):
		fleet_info= {}
		with open(aircraft_list, newline='') as x:
			aircraft_read = csv.reader(x, delimiter=',')
			for row in aircraft_read:
				if row[0] != 'code':
					fleet_info[row[0]] = (row[1], row[2], row[3], row[4])
		return fleet_info

	def build_fleet(self):
		planes = []
		for plane in self.fleet_info:
			plane = Aircraft(plane, self.fleet_info[plane][0], self.fleet_info[plane][1], self.fleet_info[plane][2], self.fleet_info[plane][3])
			planes.append(plane)
		return planes

	def __str__(self):
		return "\n".join(map(str, self.fleet))


def main():
	myFleet = Fleet()
	print(myFleet)
		
main()