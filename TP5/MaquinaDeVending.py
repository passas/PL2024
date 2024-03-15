import json

class MaquinaDeVending:

	def __init__(self):
		#Variável de Instância relativa aos produtos
		self._stock = [] # Lista de Dicionários

		#Variável de Instância relativa às moedas presentes na máquina
		self._moedeiro = {'2e': 0,
			'1e': 0,
			'50c': 0,
			'20c': 0,
			'10c': 0,
			'5c': 0,
		}
		#Variável relativa ao saldo da operação
		self._saldo = 0.0 #euros -float-
	

	#Ordenar produtos por código	
	def ordenar_por_codigo (self):
		self._stock = sorted(self._stock, key=lambda dicionario: dicionario['cod'])


	#Carregar a lista de produtos segundo um formato JSON
	def load_produtos_json (self, json_name):
		try:
			with open(json_name, 'r') as dao_json:
				if dao_json:
					self._stock = json.load (dao_json)
			#Ordenar
			self.ordenar_por_codigo()
		except:
			pass


	#Exportar a lista de produtos segundo um formato JSON
	def save_produtos_json (self, json_name):
		with open(json_name, 'w', encoding='utf8') as dao_json:
			json.dump(self._stock, dao_json, ensure_ascii=False, indent=4)


	#Carregar o estado do moedeiro segundo um formato JSON
	def load_moedeiro_json (self, json_name):
		try:
			with open(json_name, 'r') as dao_json:
				self._moedeiro = json.load (dao_json)
		except:
			pass


	#Gravar o estado do moedeiro segundo um formato JSON
	def save_moedeiro_json (self, json_name):
		with open(json_name, 'w', encoding='utf8') as dao_json:
			json.dump(self._moedeiro, dao_json, ensure_ascii=False, indent=4)


	#Convertêr saldo em string
	def get_saldo (self):
		saldo_centimos = self._saldo * 100
		centimos = saldo_centimos % 100
		euros = (saldo_centimos - centimos) / 100
		euros = int (euros)
		centimos = int (centimos)
		return f'{euros}e{centimos}c'

	#Devolvêr uma cópia -deep- do estado intero relativo aos produtos
	def get_stock (self):
		deep_stock = []

		for entrada in self._stock:
			deep_stock.append (entrada.copy())

		return deep_stock


	#Devolvêr uma cópia -deep- do estado interno relativo ao moedeiro
	def get_moedeiro (self):
		deep_moedeiro = {}

		for chave, valor in self._moedeiro.items():
			deep_moedeiro[chave] = valor

		return deep_moedeiro


	#Inserir uma moeda na máquina
	def insere_moeda (self, moeda):
		#Tabela de conversão: moeda -> saldo em euros
		conversor = {'2e': 2.0,
			'1e': 1.0,
			'50c': 0.5,
			'20c': 0.2,
			'10c': 0.1,
			'5c': 0.05,
		}
		
		#Aumentar saldo da operação
		self._saldo += conversor[moeda]

		#Aumentar número de moedas na máquina
		self._moedeiro[moeda] += 1


	#Verificar se o código corresponde a um produto
	def codigo_valido (self, cod_produto):
		for entrada in self._stock:
			if cod_produto == entrada['cod']:
				return True

		return False


	#Verificar a existência de saldo para efetuar a operação
	def saldo_bom (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if self._saldo >= entrada['preco']:
					return True

		return False


	#Quantificar valor disponível para troco da operação
	def get_troco (self):
		#Tabela de conversão: moeda -> euros
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

	#Validar se há troco relativo à operação
	def ha_troco (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if self._saldo >= entrada['preco']:
					
					excedente = self._saldo - entrada['preco']
					
					if (excedente <= self.get_troco()):
						return True
					else:
						return False



	def get_preco (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				saldo_centimos = entrada['preco'] * 100
				centimos = saldo_centimos % 100
				euros = (saldo_centimos - centimos) / 100
				euros = int (euros)
				centimos = int (centimos)
				return f'{euros}e{centimos}c'

	#Validar se existe stock do produto
	def ha_stock (self, cod_produto):
		for entrada in self._stock:
			if cod_produto in entrada['cod']:
				if entrada['quant'] > 0:
					return True
				else:
					return False


	#Comprar um produto
	def retira_produto (self, cod_produto):
		if self.codigo_valido (cod_produto):
			if self.ha_stock (cod_produto):
				if self.saldo_bom (cod_produto):
					if self.ha_troco (cod_produto):

						for entrada in self._stock:
							if cod_produto in entrada['cod']:
								entrada['quant'] -= 1
								#Problemas nos arredondamentos: cálculos c/ inteiros...
								centimos = entrada['preco'] * 100
								centimos_saldo = self._saldo * 100
								self._saldo = (centimos_saldo - centimos) / 100
								
								nome = entrada['nome']
								return f'Pode retirar o produto dispensado \"{nome}\"'
					else:
						return "Não há troco."
				else:
					return "Saldo insuficiente..."
			else:
				return "Stock inexistente..."
		else:
			return "Código inválido!"


	#Montar o troco
	def monta_troco (self):
		#Tabela de conversão: moeda -> euros
		conversor = {'2e': 2.0,
			'1e': 1.0,
			'50c': 0.5,
			'20c': 0.2,
			'10c': 0.1,
			'5c': 0.05,
		}

		troco_moedas = {'2e': 0,
			'1e': 0,
			'50c': 0,
			'20c': 0,
			'10c': 0,
			'5c': 0,
		}

		#Percorrer as moedas da mais alta para a mais baixa
		for moeda in self._moedeiro:
			#Existe dinheiro do cliente na máquina e moeda para fazêr o troco
			while (self._saldo > 0.0) and (self._moedeiro[moeda] > 0):
				
				#Se a moeda não fizer com que a máquina dê dinheiro ao cliente (que não é dele)
				if (self._saldo - conversor[moeda]) >= 0.0:
					#Decrementar saldo
					#Problemas nos arredondamentos: cálculos c/ inteiros...
					centimos = conversor[moeda] * 100
					centimos_saldo = self._saldo * 100
					self._saldo = (centimos_saldo - centimos) / 100

					#Decrementar moeda do moedeiro
					self._moedeiro[moeda] -= 1

					#Devolver moeda no troco
					troco_moedas[moeda] += 1

				#Se a moeda fizer com que a máquina dê dinheiro ao cliente (que não é dele), inrrompêr para o próximo carro de moedas...
				else:
					break

		return troco_moedas
