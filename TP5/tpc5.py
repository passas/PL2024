import sys
import re
import ply.lex as lex

import datetime

import MaquinaDeVending


maquina = MaquinaDeVending.MaquinaDeVending()
maquina.load_produtos_json ("produtos.json")
maquina.load_moedeiro_json ("moedeiro.json")



# Lista dos nomes dos tokens reconhecidos
tokens = [
   'LISTAR',
   'MOEDA',
   'SELECIONAR',
   'SALDO',
   'SAIR',
]


def t_LISTAR(lexToken):

    r'(?i)LISTAR'

    print ("maq:")
    print (f'cod\t| nome\t| quantidade\t| preço')
    print (f'----------------------------------')
    for entrada in maquina.get_stock():
        cod = entrada['cod']
        nome = entrada['nome']
        quantidade = entrada['quant']
        preco = entrada['preco']
        print (f'{cod}\t{nome}\t{quantidade}\t{preco}')



def t_MOEDA(tok):

    r'MOEDA\s((2e|1e|50c|20c|10c|5c)[\s,]+)*((2e|1e|50c|20c|10c|5c)[\s.]*)'

    moedas = re.findall (r'2e|1e|50c|20c|10c|5c', tok.value)

    for moeda in moedas:
        maquina.insere_moeda (moeda)

    print (f'maq: Saldo = {maquina.get_saldo()}')


#Tratar do token SELECIONAR
def t_SELECIONAR(tok):

    r'SELECIONAR\s(A\d+)'
    
    produto = re.search (r'A\d+', tok.value)
    produto = produto.group(0)

    warning = maquina.retira_produto (produto)
    print (warning)

    if warning == "Saldo insuficiente...":
        print (f'maq: Saldo = {maquina.get_saldo()}; Pedido = {maquina.get_preco(produto)}')




def t_SALDO(tok):

    r'(?i)SALDO'

    print (f'maq: Saldo = {maquina.get_saldo()}')


#Tratar do token RULE
def t_SAIR(lexToken):

    r'(?i)SAIR'
    
    print ("maq: Pode retirar o troco:")
    for k,v in maquina.monta_troco().items():
        if v > 0:
            print (f'{v}x {k} ')



#Tratar de um newline
def t_newline(lexToken):

    r'\n+'

    lexToken.lexer.lineno += len(lexToken.value)


#Ignorar caractéres
t_ignore  = ' \t'


#Tratar erro (caractér a caractér)
def t_error(lexToken):
    #Informar
    print("Illegal character '%s'" % lexToken.value[0])
    #Descartar
    lexToken.lexer.skip(1)





#Main
if __name__ == '__main__':

    #for entrada in maquina.get_stock():
    #    print (entrada)
    dia_de_hoje = datetime.datetime.now()
    dia_de_hoje_str = dia_de_hoje.strftime("%A, %B %d of %Y")
    print (f'maq: {dia_de_hoje_str}, Stock carregado, Estado atualizado.')
    if (dia_de_hoje.hour > 18):
        boas = "Boa noite."
    elif (dia_de_hoje.hour > 12):
        boas = "Boa tarde."
    elif (dia_de_hoje.hour > 6):
        boas = "Bom dia."

    print (f'{boas} Estou disponível para atender o seu pedido.')

    #Construir objeto lexer
    lexer = lex.lex()

    linha = input ('>> ')

    #Tratar linha do terminal -stdin-
    while linha != "":
        
        #Tokenize linha e guardar os tokens no objeto lexer
        lexer.input(linha)

        for tok in lexer:
            pass

        linha = input ('>> ')
    
    maquina.save_moedeiro_json ("moedeiro.json")
    maquina.save_produtos_json ("produtos.json")
