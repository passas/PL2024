import sys
import re


'''   -   Cadeia de caractéres inibidores de propriedades de um dígito.   -   '''
'''
#Expressão Regular que captura um dígito -\d-
digito = r'\d+'


# Expressão Regular que captura: (1) um dígito -\d- (parte inteira),
# (2) e a possíbilidade -?- de captuar a parte real -.\d-.
#
# A expressão é dividida em grupos de captura com o intuíto de escrutínio separado a cada uma das suas partes.
digito_real = r'(\d+)((.)(\d+))?'


# Expressão Regular que captura: (1) um dígito -\d- (parte inteira),
# (2) e a possíbilidade -?- de captuar o sinal deste -[\+\-].
#
# A expressão é dividida em grupos de captura com o intuíto de escrutínio separado de cada uma das suas partes.
digito_sinal = r'([\+\-])?( )?(\d+)'


# Expressão Regular que: (1) captura um dígito -\d- (parte inteira),
# (2) a possíbilidade -?- de captuar o sinal deste -[\+\-],
# (3) a possíbilidade -?- de captuar a parte real -.\d-.
#
# A expressão é dividida em grupos de captura com o intuíto de escrutínio separado a cada uma das suas partes.
digito_real_sinal = r'([\+\-])?( )?((\d+)((.)(\d+)))?'
'''
'''  .  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   .     '''


# - Definição de Tokens -

#regex_soma = r'\d+'
#regex_ligar = r'[Oo][Nn]'
#regex_desligar = r'[Oo][Ff]{2}'
#regex_display = r'='

#(1) Composição de Tokens, e (2) Nomeação de Tokens
input_regex = r'(?P<soma>\d+)|(?P<ligar>[Oo][Nn])|(?P<desligar>[Oo][Ff]{2})|(?P<display>=)'




#Main
if __name__ == '__main__':

	#Estado que define o comportamento do somatório: (1) ligado, (2) desligado.
	somatorio_ligado = True
	#Variável que comporta o valor do somatório
	somatorio = 0

	#Enquanto não encontrar o EOF... - Ctrl+D -
	for linha in sys.stdin:

		#Processar linha: encontrar todos os tokens presentes na linha, e compô-los num match object (guardando-os numa lista)
		lista_de_object_matches = re.finditer (input_regex, linha)
			
		#Percorrer a lista de Match Objects
		for object_match in lista_de_object_matches:
			 #Tratar Match Object

			 #Encontrei um dígito
			 if object_match.lastgroup == 'soma':
			 	#O comportamento do somatório -somatorio_ligado_ está ligado
			 	if somatorio_ligado == True:
			 		#Converter -string- num -int- e somar ao somatório -somatorio-
			 		somatorio += int (object_match.group('soma'))
			 
			 #Encontrei uma instrução para ligar o comportamento do somatório
			 elif object_match.lastgroup == 'ligar':
			 	#Ligar o comportamento do somatório
			 	somatorio_ligado = True
			 
			 #Encontrei uma instrução para desligar o comportamento do somatório
			 elif object_match.lastgroup == 'desligar':
			 	#Desligar o comportamento do somatório
			 	somatorio_ligado = False
			 
			 #Encontrei uma instrução para exibir o resultado do somatório
			 elif object_match.lastgroup == 'display':
			 	#-stdin-: Imprimir resultado do somatório.
			 	print (f'Soma = {somatorio}')
