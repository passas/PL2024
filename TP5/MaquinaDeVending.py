import json

class MaquinaDeVending:

	def __init__(self):
		self._stock = []


	def load_json (self, json_name):
		with open(json_name, 'r') as dao_json:
			self._stock = json.load (dao_json)


	def save_json (self, json_name):
		with open(json_name, 'w', encoding='utf8') as dao_json:
			json.dump(self._stock, dao_json, ensure_ascii=False, indent=4)


	def get_stock (self):
		deep_stock = []

		for entrada in self._stock:
			deep_stock.append (entrada.copy())

		return deep_stock
