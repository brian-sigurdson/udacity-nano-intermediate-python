import json
import helper


def load_nobel_prizes(filename="prize.json"):
	with open(filename, 'r') as infile:
		contents = json.load(infile)

	return contents


def year_and_category(data, year, category):
	for key in data.keys():
		for item in data[key]:
			if item['year'] == year and item['category'] == category:
				print(f"Year = {item['year']}; Category = {item['category']}")


def all_years_all_categories(data):
	for key in data.keys():
		for item in data[key]:
			print(f"Year = {item['year']}; Category = {item['category']}")


def a_year(data, year):
	for key in data.keys():
		for item in data[key]:
			if item['year'] == year:
				print(f"Year = {item['year']}; Category = {item['category']}")


def a_category(data, category):
	for key in data.keys():
		for item in data[key]:
			if item['category'] == category:
				print(f"Year = {item['year']}; Category = {item['category']}")


def main(year, category):
	data = load_nobel_prizes()
	if year is not None and category is not None:
		year_and_category(data, year, category)

	if year is None and category is None:
		all_years_all_categories(data)

	if year is not None and category is None:
		a_year(data, year)

	if year is None and category is not None:
		a_category(data, category)


if __name__ == '__main__':
	parser = helper.build_parser()
	args = parser.parse_args()
	main(args.year, args.category)
