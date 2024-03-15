
# Vending Machine

```Sérgio Miguel Cabral Passinhas dos Santos Costa :: A81215```

## Conteúdo
+ Tree
+ How-To
+ Objetivo do Trabalho
+ Abstract
+ Trabalho Futuro

## Tree
Primeira utilização:
```
.
├── MaquinaDeVending.py
├── produtos.json
└── tpc5.py
```
Primeira e posterior utilização:
```
.
├── MaquinaDeVending.py
├── moedeiro.json
├── produtos.json
└── tpc5.py
```
## How-To

```$ python3 tpc5.py```\
A partir daqui seguem-se os comandos válidos do enunciado.\
*Explicitar comandos válidos*

## Objetivo do Trabalho
O objetivo desta resolução é explorar as potencialidades da análise léxica na validação de *input* num programa.\
O progrma *per se* visa, por sua vez, explorar algumas técnicas de engenharia de software em python. Chamo em destaque a programação orientada a objectos, nomeadamente na classe que acarreta o estado e comportamento da Vending Machine; a mesma, por questões lúdicas, acarta computações relacionadas com cópias íntegras -deep- de coleções.\
\
O trabalho segue uma separação Controlador-Model-Viewer, sendo que o Controlador e o Viewer encontram-se fundidos em ```tpc5.py``` e o Model em ```MaquinaDeVending.py```.\
Segue uma persistência dos produtos e do moedeiro (estado do número de moedas na máquina) em ficheiros json. O stock só consegue ser alterado a partir deste ficheiro.

## Abstract

## Trabalho Futuro
```
> Operações de saldo e preços em cêntimos; arredondamentos bugam o estado do programa.
```
