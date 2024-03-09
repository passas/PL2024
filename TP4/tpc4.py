import sys
import ply.lex as lex


# Lista dos nomes dos tokens reconhecidos
tokens = [
   'SELECT',
   'ID',
   'FROM',
   'WHERE',
   'RULE',
   'PARAMETER',
]


#Tratar do token SELECT
def t_SELECT(lexToken):
    #Definir
    r'(?i)SELECT'

    #Devolver
    return lexToken


#Tratar do token FROM
def t_FROM(lexToken):
    #Definir
    r'(?i)FROM'
    
    #Devolver
    return lexToken


#Tratar do token WHERE
def t_WHERE(lexToken):
    #Definir
    r'(?i)WHERE'
    
    #Devolver
    return lexToken


#Tratar do token RULE
def t_RULE(lexToken):
    #Definir
    r'(?i)(>=)|(=>)|(<=)|(=<)|(==)|(>)|(<)|(=)'
    
    #Devolver
    return lexToken


#Tratar do token ID
def t_ID (lexToken):
    #Definir
    r'[a-zA-Z_][a-zA-Z_0-9]*([,]?)'

    #Devolver
    return lexToken


#Tratar do token PARAMETER
def t_PARAMETER (lexToken):
    #Definir
    r'(([a-zA-Z_][a-zA-Z_0-9]*)|(\d+))([,]?)'

    #Devolver
    return lexToken


#Tratar de um newline
def t_newline(lexToken):
    #Definir
    r'\n+'

    #Atuar
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

    #Construir objeto lexer
    lexer = lex.lex()
    
    #Tratar linha do terminal -stdin-
    for linha in sys.stdin:
    
        #Tokenize linha e guardar os tokens no objeto lexer
        lexer.input(linha)
        
        #Percorrer os tokens encontrados e guardados no objeto lexer
        for tok in lexer:
            #-stdout-: (1) Tipo do token, e (2) conteúdo do token
            print (f'{tok.type}: {tok.value}')
            
            '''
            Conjunto de operações plausíveis sobre o objeto token -LexToken-
            #print(tok)
            #print(tok.type, tok.value, tok.lineno, tok.lexpos)
            '''
            
