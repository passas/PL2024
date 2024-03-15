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


	def insere_moeda (self, moeda):
		conversor = {'2e': 2.0,
			'1e': 1.0,
			'50c': 0.5,
			'20c': 0.2,
			'10c': 0.1,
			'5c': 0.05,
		}
		
		self._saldo += conversor[moeda]

		self._moedeiro[moeda] += 1


	def codigo_valido (self, cod_produto):
		for entrada in self._stock:
			if cod_produto == entrada['cod']:
				return True

		return False


	def saldo_bom (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if self._saldo >= entrada['preco']:
					return True

		return False

	def get_troco (self):
		conversor = {'2e': 2.0,
			'1e': 1.0,
			'50c': 0.5,
			'20c': 0.2,
			'10c': 0.1,
			'5c': 0.05,
		}

		troco = 0.0
		for k,v in self._moedeiro.items():
			if v > 0:
				troco += v * conversor[k]

		return troco

	def ha_troco (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if self._saldo >= entrada['preco']:
					
					excedente = self._saldo - entrada['preco']
					
					if (excedente <= self.get_troco()):
						return True
					else:
						return False

	def ha_stock (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if entrada['quant'] > 0:
					return True
				else:
					return False


	def retira_produto (self, cod_produto):
		if self.codigo_valido (cod_produto):
			if self.ha_stock (cod_produto):
				if self.saldo_bom (cod_produto):
					if self.ha_troco (cod_produto):

						for entrada in self._stock:
							if cod_produto in entrada['cod']:
								entrada['quant'] -= 1
