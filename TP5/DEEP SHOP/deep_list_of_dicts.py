import json

#abrir ficheiro -leitura-
with open ('produtos.json', 'r') as dao_json:
	#carregar ficheiro
	data = json.load (dao_json)

deep = []

for entrada in data:
	deep.append (entrada.copy())

data[0]['cod'] = "A0"

for entrada in data:
	print (entrada['cod'])
	#print (entrada['nome'])
	#print (entrada['quant'])
	#print (entrada['preco'])

for entrada in deep:
	print (entrada['cod'])
	#print (entrada['nome'])
	#print (entrada['quant'])
	#print (entrada['preco'])
