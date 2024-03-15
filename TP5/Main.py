import MaquinaDeVending

#Main
if __name__ == '__main__':

	maquina = MaquinaDeVending.MaquinaDeVending()

	maquina.load_json ("produtos.json")

	for stock in maquina.get_stock():
		print (stock)

	print (maquina.get_saldo())
	print (maquina.get_moedeiro())

	print (maquina.get_saldo())
	maquina.insere_moeda ('50c')
	maquina.insere_moeda ('10c')

	

	print (f'Tem A000? {maquina.codigo_valido("A000")}')

	for entrada in maquina.get_stock():
		check = entrada['cod']
		checked = maquina.codigo_valido(entrada['cod'])
		print (f'Tem {check}? {checked}')
		bom = maquina.saldo_bom(entrada['cod'])
		print (f'Posso comprar? {bom}')

	print (maquina.get_saldo())
	print (maquina.get_moedeiro())
	
	warning = maquina.retira_produto ("A23")
	if warning:
		print (warning)

	print (maquina.get_saldo())
	print (maquina.get_moedeiro())

	print ("SAIR...")
	for k,v in maquina.monta_troco().items():
		if v > 0:
			print (f'{v}x {k} ')


	print (maquina.get_saldo())
	print (maquina.get_moedeiro())

	maquina.save_json ("produtos.json")
