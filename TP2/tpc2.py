import sys
import re


#H1 MarkDown
md_heading_1 = r'# (.*)'
#H1 HTML -conversor-
html_heading_1 = r'<h1>\1</h1>'


#H2 MarkDown
md_heading_2 = r'## (.*)'
#H2 HTML -conversor-
html_heading_2 = r'<h2>\1</h2>'


#H3 MarkDown
md_heading_3 = r'### (.*)'
html_heading_3 = r'<h3>\1</h3>'



'''Mecanismo -Isomorfismo- para restituir Headers inválidos'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
''' 
      Texto markdown: #### Título    -md_heading_invalid-
      Transformado em: <####>Título</####>    -html_heading_invalid- 
      
      (...)
      
      No final da tradução (Markdown - HTML) dos cabeçalhos, restituição dos cabeçalhos (inválidos).
      
      <####>Título</####>    -html_invalid_isomorfismo-
      #### Título    -md_headig_invalid_isomorfismo-
'''
#H_Invalid MarkDown
md_heading_invalid = r'(#{4,}) (.*)'
#H_Invalid HTML -conversor-
html_heading_invalid = r'<\1>\2</\1>'
#H_Invalid HTML
html_heading_invalid_iso = r'<(#{4,})>(.*?)</\1>'
#H_Invalid MarkDown -conversor-
md_heading_invalid_iso = r'\1 \2'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



#Bold MarkDown
md_bold = r'\*\*(.*)\*\*'
#Bold HTML -conversor-
html_bold = r'<strong>\1</strong>'


#Italic MarkDown
md_italic = r'\*(.*)\*'
#Italic HTML -conversor-
html_italic = r'<em>\1</em>'


#BlockQuote MarkDown
md_block_quote = r'> (.*)'
#BlockQuote HTML -conversor-
html_block_quote = r'<blockquote>\1</blockquote>'


#Lista Desordenada Markdown    (Conversão HTML feita através de uma função)
md_list_unordered = r'([ ]?- (.*)\n?)+'
#Lista Ordenada Markdown    (Conversão HTML feita através de uma função)
md_list_ordered = r'([ ]?\d+\. (.*)\n?)+'


#Code MarkDown
md_code = r'`(.*)`'
#Code HTML -conversor-
html_code = r'<code>\1</code>'


#Image MarkDown
md_image = r'!\[(.*?)\]\((.*?)\)'
#Image HTML -conversor-
html_image = r'<img src="\2" alt="\1">'


#Link MarkDown
md_link = r'\[(.*?)\]\((.*?)\)'
#Link HTML -conversor-
html_link = r'<a href="\2">\1</a>'




#Função, que dado um Objeto de Match -match_object-, de uma expressão regular de uma lista desordenada,
#transforma-a, e dá como resultado a sua conversão em HTML -string- -resultado-
def processa_lista_unordered (match_object):
  #Variável que guarda o resultado da conversão MarkDown para HTML -string-
  resultado = "<ul>" #Abrir tag da lista desordenada

  #Retirar os NewLine's -\n- dos itens capturados, e guardá-los numa lista -[string]-
  lista_de_items_md = match_object.string.split ('\n')

  #Variável que guarda a substituição do MarkDown (- string) para o HTML (<li>string</li>)
  lista_de_items_html = []

  #Expressão regular que diz respeito a um item (desordenado) em MarkDown
  er_md_item = r'([ ]?- (.*)\n?)+'
  #Expressão regular que diz respeito a um item em HTML, mediante a captura supra
  er_html_item = r'  <li>\2</li>'

  #Percorrer a lista dos itens em MarkDown (sem o newline)
  for item in lista_de_items_md:
    #Capturar o item em MarkDown -er_md_item-, convertê-lo em HTML -er_html_item-, e guardar o resultado numa lista [string]
    lista_de_items_html.append (re.sub (er_md_item, er_html_item, item))
  
  #Percorrer a lista dos items em HTML
  for item in lista_de_items_html:
    #Montar string resultante
    resultado += "\n" + item

  #Fechar tag da lista desordenada
  resultado += "</ul>"

  #Devolver conversão HTML -string-
  return resultado




#Função, que dado um Objeto de Match -match_object-, de uma expressão regular de uma lista ordenada,
#transforma-a, e dá como resultado a sua conversão em HTML -string- -resultado-
def processa_lista_ordered (match_object):
  #Variável que guarda o resultado da conversão MarkDown para HTML -string-
  resultado = "<ol>\n" #Abrir tag da lista ordenada

  #Retirar os NewLine's -\n- dos itens capturados, e guardá-los numa lista -[string]-
  lista_de_items_md = match_object.string.split ('\n')

  #Variável que guarda a substituição do MarkDown (- string) para o HTML (<li>string</li>)
  lista_de_items_html = []

  #Expressão regular que diz respeito a um item (ordenado) em MarkDown
  er_md_item = r'([ ]?\d+\. (.*))+'
  #Expressão regular que diz respeito a um item em HTML, mediante a captura supra
  er_html_item = r'  <li>\2</li>'

  #Percorrer a lista dos itens em MarkDown (sem o newline)
  for item in lista_de_items_md:
    #Capturar o item em MarkDown -er_md_item-, convertê-lo em HTML -er_html_item-, e guardar o resultado numa lista [string]
    lista_de_items_html.append (re.sub (er_md_item, er_html_item, item))
  
  #Percorrer a lista dos items em HTML
  for item in lista_de_items_html:
    #Montar string resultante
    resultado += item + "\n"

  #Fechar tag da lista ordenada
  resultado += "</ol>"

  #Devolver conversão HTML -string-
  return resultado






#Main
if __name__ == '__main__':

  
  #Enquanto não for lido o EOF -Ctrl+D-, processar linha
  for linha in sys.stdin:

    #Transformar a linha numa síntaxe de exceção para lidar com Headers inválidos
    linha = re.sub (md_heading_invalid, html_heading_invalid, linha)

    #Processar os Headers nível 3 da linha
    linha = re.sub (md_heading_3, html_heading_3, linha)
    
    #Processar os Headers nível 2 da linha
    linha = re.sub (md_heading_2, html_heading_2, linha)

    #Processar os Headers nível 1 da linha
    linha = re.sub (md_heading_1, html_heading_1, linha)

    #Repôr os Headers (inválidos) em Markdown
    linha = re.sub (html_heading_invalid_iso, md_heading_invalid_iso, linha)

    #Processar os Bold da linha
    linha = re.sub (md_bold, html_bold, linha)

    #Processar os Itálicos da linha
    linha = re.sub (md_italic, html_italic, linha)

    #Processar as Block Quotes da linha
    linha = re.sub (md_block_quote, html_block_quote, linha)

    #Processar as Listas Desordenadas da linha
    # Problema (2024-02-20) os itens desordenados não se processam à linha!
    linha = re.sub (md_list_unordered, processa_lista_unordered, linha)

    #Processar as Listas Ordenadas da linha
    # Problema (2024-02-20) os itens ordenados não se processam à linha!
    linha = re.sub (md_list_ordered, processa_lista_ordered, linha)

    #Processar o Código na linha
    # Problema (2024-02-20) o código pode abranger múltiplas linhas...
    linha = re.sub (md_code, html_code, linha)

    #Processar a Imagem na linha
    linha = re.sub (md_image, html_image, linha)
    
    #Processar o Link na linha
    linha = re.sub (md_link, html_link, linha)


    #-stdout-: Imprimir as alterações feitas na linha.
    print (linha)
