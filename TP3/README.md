# Somador On/Off

```Sérgio Miguel Cabral Passinhas dos Santos Costa :: A81215```

## Conteúdo
+ Tree
+ How-To
+ Abstract
+ Referências

## Tree
```
.
├── Object Oriented
│   ├── Calculadora.py
│   └── inputer.py
└── tpc3.py
```
## How-To

```$ python3 tpc3.py```

```$ python3 tpc3.py < file```

\
\
_No caso de estarmos dentro da directoria Object Oriented:_

```$ python3 inputer.py```

```$ python3 inputer.py < file```


## Abstract

* Eu monto um tokenizer: para cada expressão regular, nomeio-a \[1\].\
Faço a procura de todos os padrões numa linha com o ```re.finditer``` \[2\], que me dá os Match Object capturados na linha, por ordem; gravo-os numa lista.\
Itero a lista de Match Object's, e procedo à ação respetiva, mediante o nome da captura em causa ```match_object.lastgroup``` \[3\].\
\
_Nota:_ A minha expressão regular é um grupo de captura, onde engloba várias expressões regulares singulares, nomeadas.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para isso utilizei a propriedade de ```Match.group``` \[1\].


* O comportamento do somatório começa por estar ativo, aquando de uma captura de um dígito(s), a mesma é convertida para o homólogo em inteiro ```ìnt (...)``` e somada.\
O comportamento é desligado aquando da captura do token respetivo, volta a ser retomado se indicado.\
Em relação ao somatório, a informação do mesmo é imprimida no ecrã sempre que encontra o token respetivo à ordem em questão.\

\
\
**Nota Pessoal**\
\
Decidi abordar também o paradigma orientado aos objetos, onde nesse caso, o parsing do input é feito de igual modo, à exceção de que as ações (e neste caso, a lógica do programa), é controlada através de um objeto -Calculadora-.

## Referências
\[1\] [Match.group](https://docs.python.org/pt-br/3/library/re.html#re.Match.group)

\[2\] [re.finditer](https://docs.python.org/pt-br/3/library/re.html#re.finditer)

\[3\] [Tokenizer](https://docs.python.org/pt-br/3/library/re.html#writing-a-tokenizer)
