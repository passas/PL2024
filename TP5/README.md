* Intendo:

  > Montar um objeto referente à máquina de vending: (1) estado e (2) comportamento. Numa fase inicial, o próprio 'DAO' estará inserido dentro da própria classe. O DAO é referente à leitura e escrita dos dados da máquina em ficheiro(s) JSON.

  > O interpretador de comandos será, nesta fase, codificado na main através de um tokenizer (ou lexer, mediante a complexidade e inteligibilidade do código).

 * Objetivo:

   > Mantêr o programa coeso e pequeno.

\
\
**To Do:**
```
> Ingestor de moedas na vending machine: conversão/tradução de moedas em saldo;

> Adicionar compra de um produto à vending machine;

> Algoritmo de troco do moedeiro;

> Pretty-print do stock da Vendind Machine;

> Interpretador de comandos da vending machine -REGEX-.
```


```
 - MANIFESTO -

O objetivo desta resolução é explorar as potencialidades da análise léxica na validação de *input* num programa.
O progrma *per se* visa, por sua vez, explorar algumas técnicas de engenharia de software em python. Chamo em destaque a programação orientada a objectos, nomeadamente na classe que acarreta o estado e comportamento da Vending Machine; a mesma, por questões lúdicas, acarta computações relacionadas com cópias íntegras -deep- de coleções.
```
