import json


def load_cad(filename="data_sets/cad.json"):
	with open(filename, 'r') as infile:
		return json.load(infile)


contents = load_cad()


for item in contents['data']:
	if item[0] == '2002 PB' and item[3].startswith('2000-Jan-01'):
		print(item)

