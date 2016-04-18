from airport import AirportInfo, Airport
import random

class Destinations:

	def __init__(self):
		airports = AirportInfo()
		self._poss_dest = airports.airports
		self._home_airport = Airport('599', 'Dublin', 'Dublin', 'Ireland', 53.421333,-6.270075, 'Euro')
		self._dest = self.get_destinations()
		

	def get_destinations(self):
		destinations = [self._home_airport]
		for i in range(4):
			destination = self._poss_dest[random.randint(0, len(self._poss_dest) + 1)]
			destinations.append(destination)
		return destinations

	def __str__(self):
		return "\n".join(map(str, self._dest))

print(Destinations())