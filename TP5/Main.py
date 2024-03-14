import MaquinaDeVending

#Main
if __name__ == '__main__':

	maquina = MaquinaDeVending.MaquinaDeVending()

	maquina.load_json ("produtos.json")

	for stock in maquina.get_stock():
		print (stock)

	maquina.save_json ("teste_save_json.json")
