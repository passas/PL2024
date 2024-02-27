import sys
import re

import Calculadora


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

#Composição de Tokens e Nomeação dos Tokens
input_regex = r'(?P<soma>\d+)|(?P<ligar>[Oo][Nn])|(?P<desligar>[Oo][Ff]{2})|(?P<display>=)'




#Main
if __name__ == '__main__':

	#Objecto que comporta uma calculadora como entidade computacional
	calculadora = Calculadora.Calculadora()
	#Ligar o comportamento da calculadora
	calculadora.liga()

	#Enquanto não encontrar o EOF... - Ctrl+D -
	for linha in sys.stdin:

		#Processar linha: encontrar todos os tokens presentes na linha, e compô-los num match object (guardando-os numa lista)
		lista_de_object_matches = re.finditer (input_regex, linha)
		
		#Percorrer a lista de Match Objects
		for object_match in lista_de_object_matches:
			 #Tratar Match Object
			 
			 #Encontrei um dígito
			 if object_match.lastgroup == 'soma':
			 	#Converter a -string- para um -int- e enviar a mensagem ao objecto
			 	calculadora.soma ( int (object_match.group('soma')) )
			 
			 #Encontrei uma instrução para ligar o comportamento do somatório
			 elif object_match.lastgroup == 'ligar':
			 	#Enviar (a respetiva) mensagem ao objeto
			 	calculadora.liga ()
			 
			 #Encontrei uma instrução para desligar o comportamento do somatório
			 elif object_match.lastgroup == 'desligar':
			 	#Enviar (a respetiva) mensagem ao objeto
			 	calculadora.desliga ()
			 
			 #Encontrei uma instrução para exibir o resultado do somatório
			 elif object_match.lastgroup == 'display':
			 	#-stdin-: Enviar a mensagem (respetiva) ao objeto, e imprimir o seu conteúdo.
			 	print (f'Soma = {calculadora.get_soma()}')
