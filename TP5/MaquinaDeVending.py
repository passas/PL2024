import json

class MaquinaDeVending:

	def __init__(self):
		self._stock = []
		self._moedeiro = {'2e': 0,
			'1e': 0,
			'50c': 0,
			'20c': 0,
			'10c': 0,
			'5c': 0,
		}
		self._saldo = 0.0 #euros -float-


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

	def get_moedeiro (self):
		deep_moedeiro = {}

		for chave, valor in self._moedeiro.items():
			deep_moedeiro[chave] = valor

		return deep_moedeiro
