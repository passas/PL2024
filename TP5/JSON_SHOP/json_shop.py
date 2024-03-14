import json


#abrir ficheiro -leitura-
with open ('produtos.json', 'r') as dao_json:
	#carregar ficheiro
	data = json.load (dao_json)

#percêber ficheiro
for entrada in data:
	print (entrada['cod'])
	print (entrada['nome'])
	print (entrada['quant'])
	print (entrada['preco'])

# ...

#dados em memória
dados = [
	{	"cod": "A23", 
		"nome": "água 0.5L",
		"quant": 8,
		"preco": 0.5
	},
	{	"cod": "A21", 
		"nome": "sumo 0.33L",
		"quant": 2,
		"preco": 0.9
	},
	{	"cod": "A22", 
		"nome": "leite 0.33L",
		"quant": 8,
		"preco": 0.6
	}
]

#abrir ficheiro -escrita-
with open("dump_teste.json", "w", encoding='utf8') as write_file:
	#exportar json
	json.dump(dados, write_file, ensure_ascii=False, indent=4)
