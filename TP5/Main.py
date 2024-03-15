import MaquinaDeVending

#Main
if __name__ == '__main__':

	maquina = MaquinaDeVending.MaquinaDeVending()

	maquina.load_json ("produtos.json")

	for stock in maquina.get_stock():
		print (stock)

	print (maquina.get_moedeiro())

	maquina.insere_moeda ('50c')

	print (maquina.get_moedeiro())

	print (f'Tem A000? {maquina.codigo_valido("A000")}')

	for entrada in maquina.get_stock():
		check = entrada['cod']
		checked = maquina.codigo_valido(entrada['cod'])
		print (f'Tem {check}? {checked}')
		bom = maquina.saldo_bom(entrada['cod'])
		print (f'Posso comprar? {bom}')

	maquina.retira_produto ("A23")

	maquina.save_json ("produtos.json")
