import csv

class Currencies:

	currency_rates_file = 'currencyrates.csv'
	country_currency_file = 'countrycurrency.csv'

	def __init__(self, currency_list = currency_rates_file, country_currency_list = country_currency_file):
		self.currency_rate = self.get_rate(currency_list)
		self.currency_countries = self.country_currencies(country_currency_list)

	def get_rate(self, currency_list):
		rate= {}
		with open(currency_list, newline='') as x:
			currency_read = csv.reader(x, delimiter=',')
			for row in currency_read:
				rate[row[1]] = (row[-2])
		return rate

	def country_currencies(self, country_currency_list):
		country_currency = {}
		with open(country_currency_list, newline='') as y:
			country_read = csv.reader(y, delimiter=',')
			for row in country_read:
				country_currency[row[0]] = row[-3]
		return country_currency

def main():
	my_currencies = Currencies()
	print(my_currencies.currency_rate)
	print(my_currencies.currency_countries)

if __name__ == '__main__':
	main()