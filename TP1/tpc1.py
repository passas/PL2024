#_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado


#main
if __name__ == '__main__':
	#Estrutura de dados auxiliar para o histograma relativo às idades
	lista_idades = []
	#Estrutura de dados que comporta as modalidades existentes
	set_modalidades = set()
	#Estrutura de dados auxiliar para o processamento estatístico acerca dos resultados
	lista_resultados = []
	
	#Abrir ficheiro -emd.csv-
	fd_emd = open('emd.csv', 'tr') 
	
	#Descartar a linha do cabeçalho
	discard_cabecalho = fd_emd.readline()

	#Lêr linha a linha
	for linha in fd_emd:
			#Separar campos da linha (separados por vírgula)
			campos = linha.split(',') #[_id, index, ...]

			#Extraír campo relevante -idade-
			idade = campos[5]
			#Acrescentar a idade -int- à lista de idades
			lista_idades.append ( int(idade) )

			#Extraír campo relevante -modalidade-
			modalidade = campos[8]
			#Acrescentar modalidade ao conjunto
			set_modalidades.add ( modalidade )

			#Extraír campo relevante -resultado-
			#Separar a string resultado -bool- do caractér de mudança de linha -\n-
			resultado_newline = campos[12].split('\n') #[bool,'\n']
			#Adicionar a string resultado -bool- à lista de resultados
			resultado = resultado_newline[0] #bool
			lista_resultados.append ( resultado )



  

	'''Ordem lexicográfica'''
	#Ordenar dados por modalidade
	set_modalidades = sorted(set_modalidades)
	#Imprimir -stdout- modalidades ordenadas por ordem lexicográfica
	print (set_modalidades)

  



	'''Calcular estatísticas de aptidão'''
	#Variável que conta total de aptos -true-
	n_apto = 0
	#Variável que conta total de inaptos -false-
	n_inapto = 0
	#Percorrer os elementos da lista de resultados
	for resultado in lista_resultados:
		#Incrementar total de aptos
		if resultado == "true":
			n_apto += 1
		#Incrementar total de inaptos
		elif resultado == "false":
			n_inapto += 1

	#Calcular e imprimir a percentagem de atletas aptos
	print(f"Aptos: {n_apto/len(lista_resultados) * 100}%")
	#Calcular e imprimir a percentagem de atletas inaptos
	print(f"Inaptos: {n_inapto/len(lista_resultados) * 100}%")



  

	'''Histograma'''
	histograma_idades = {}
	#Limite inferior de idades
	limite_inferior = 5
	#Limite superior de idades
	limite_superior = 95
	#Intervalo entre as idades
	salto = 5
	#Percorrer de -limite inferior- até -limite superior- com um salto de -intervalo- -i-
	for i in range (limite_inferior, limite_superior, salto):
		#Definir intervalo -chave-
		intervalo = f"[{i},{i + salto}]"
		#Iniciar contador -frequências- a 0
		histograma_idades[ intervalo ] = 0
		#Percorrer a lista com as idades -Theta (N)-
		for idade in lista_idades:
			#Testar se a idade está dentro do intervalo -escalão-
			if idade >= i and idade < i + salto:
				#Aumentar a frequência dos atletas no intervalo -escalão-
				histograma_idades[ intervalo ] += 1

	#Percorrer o dicionário de frequências por chave, valor
	for intervalo, frequencia in histograma_idades.items():
		#Imprimir a frequência por intervalo
		print (f'{intervalo}: {frequencia}')		
