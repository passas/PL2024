import sys
import re

import Calculadora

'''
on = r'[Oo][Nn]'

off = r'[Oo][Ff]{2}'

igual = r'='

digito = r'\d+'

digito_real = r'\d+(.\d+)?'

digito_sinal = r'(\+\-)?( )?(\d+(.\d+)?)'

digito_real_sinal = r'(\+\-)?( )?(\d+(.\d+)?)'
'''

regex_soma = r'\d+'
regex_ligar = r'[Oo][Nn]'
regex_desligar = r'[Oo][Ff]{2}'
regex_display = r'='

input_regex = r'(?P<soma>\d+)|(?P<ligar>[Oo][Nn])|(?P<desligar>[Oo][Ff]{2})|(?P<display>=)'


#Main
if __name__ == '__main__':

	#estado = False
	#soma = 0
	calculadora = Calculadora.Calculadora()

	for linha in sys.stdin:

		lista_de_object_matches = re.finditer (input_regex, linha)
		
		for object_match in lista_de_object_matches:
			 
			 if object_match.lastgroup == 'soma':
			 	#if estado == True:
			 	#	soma += int (object_match.group('soma'))
			 	
			 	calculadora.soma ( int (object_match.group('soma')) )
			 
			 elif object_match.lastgroup == 'ligar':
			 	#estado = True
			 	calculadora.liga ()
			 elif object_match.lastgroup == 'desligar':
			 	#estado = False
			 	#soma = 0
			 	calculadora.desliga ()
			 elif object_match.lastgroup == 'display':
			 	#if estado == True:
				# 	print (soma)
			 	print (calculadora.get_soma())
