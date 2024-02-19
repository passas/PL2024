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

'''Mecanismo de Isomorfismo para restituir Headers inválidos'''
#H_Invalid MarkDown
md_heading_invalid = r'(#{4,}) (.*)'
#H_Invalid HTML -conversor-
html_heading_invalid = r'<\1>\2</\1>'
#H_Invalid HTML
html_heading_invalid_iso = r'<(#{4,})>(.*?)</\1>'
#H_Invalid MarkDown -conversor-
md_heading_invalid_iso = r'\1 \2'
'''- - -'''

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

#Lista Desordenada Markdown
md_list_unordered = r'([ ]?- (.*)\n?)+'
#Lista Ordenada Markdown
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


# Função que dado um Objeto de Match, de uma expressão regular de uma lista desordenada,
#transforma-a, e dá como resultado a conversão para HTML -string-
def processa_lista_unordered (match_object):
  #Variável que guarda o resultado da conversão -string-
  resultado = "<ul>" #Abrir tag da lista desordenada

  #Retirar os NewLine's -\n- dos items capturados, e guardá-los numa lista
  lista_de_items_md = match_object.string.split ('\n')

  #Variável que guarda a substituição do MarkDown -- *- para o HTML -<li>*</li>-
  lista_de_items_html = []

  #Expressão regular que diz respeito a um item em MarkDown
  er_md_item = r'([ ]?- (.*)\n?)+'
  #Expressão regular que diz respeito a um item em HTML, mediante a captura supra
  er_html_item = r'  <li>\2</li>'

  #Percorrer a lista dos items em MarkDown
  for item in lista_de_items_md:
    #Capturar o item em MarkDown, convertê-lo em HTML, e guardar o resultado numa lista
    lista_de_items_html.append (re.sub (er_md_item, er_html_item, item))
  
  #Percorrer a lista dos items em HTML
  for item in lista_de_items_html:
    #Montar string resultante
    resultado += "\n" + item

  #Fechar tag da lista desordenada
  resultado += "</ul>"

  #Devolver conversão -string-
  return resultado


# Função que dado um Objeto de Match, de uma expressão regular de uma lista ordenada,
#transforma-a, e dá como resultado a conversão para HTML -string-
def processa_lista_ordered (match_object):
  #Variável que guarda o resultado da conversão -string-
  resultado = "<ol>" #Abrir tag da lista ordenada

  #Retirar os NewLine's -\n- dos items capturados, e guardá-los numa lista
  lista_de_items_md = match_object.string.split ('\n')

  #Variável que guarda a substituição do MarkDown -- *- para o HTML -<li>*</li>-
  lista_de_items_html = []

  #Expressão regular que diz respeito a um item em MarkDown
  er_md_item = r'([ ]?\d+\. (.*)\n?)+'
  #Expressão regular que diz respeito a um item em HTML, mediante a captura supra
  er_html_item = r'  <li>\2</li>'

  #Percorrer a lista dos items em MarkDown
  for item in lista_de_items_md:
    #Capturar o item em MarkDown, convertê-lo em HTML, e guardar o resultado numa lista
    lista_de_items_html.append (re.sub (er_md_item, er_html_item, item))
  
  #Percorrer a lista dos items em HTML
  for item in lista_de_items_html:
    #Montar string resultante
    resultado += "\n" + item

  #Fechar tag da lista desordenada
  resultado += "</ol>"

  #Devolver conversão -string-
  return resultado



#Main
if __name__ == '__main__':
  
  #Enquanto não for lido o EOF -Ctrl+D-, processar linha
  for linha in sys.stdin:

    linha = re.sub (md_heading_invalid, html_heading_invalid, linha)

    linha = re.sub (md_heading_3, html_heading_3, linha)
    
    linha = re.sub (md_heading_2, html_heading_2, linha)

    linha = re.sub (md_heading_1, html_heading_1, linha)

    linha = re.sub (html_heading_invalid_iso, md_heading_invalid_iso, linha)

    linha = re.sub (md_bold, html_bold, linha)

    linha = re.sub (md_italic, html_italic, linha)

    linha = re.sub (md_block_quote, html_block_quote, linha)

    linha = re.sub (md_list_unordered, processa_lista_unordered, linha)

    linha = re.sub (md_list_ordered, processa_lista_ordered, linha)

    linha = re.sub (md_code, html_code, linha)

    linha = re.sub (md_image, html_image, linha)
    
    linha = re.sub (md_link, html_link, linha)

    print (linha)
