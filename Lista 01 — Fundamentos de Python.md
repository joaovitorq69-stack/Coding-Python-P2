## LISTA 01 — FUNDAMENTOS DE PYTHON

Disciplina: Coding — Python

Professor(a): Ana Paula do Ó

Lista: 01 — Fundamentos de Python

Quantidade: 20 exercícios

## Orientações ao aluno

- 1. Resolva os exercícios utilizando Python.

- 2. Os programas devem ser escritos pelo próprio aluno.

- 3. Utilize somente os comandos e conceitos trabalhados em aula.

- 4. Evite utilizar recursos que ainda não foram estudados.

- 5. Todos os programas devem ser testados antes da entrega.

- 6. O código deve estar organizado e apresentar mensagens claras para o usuário.

- 7. Durante a aula, o professor poderá solicitar que o aluno explique e modifique qualquer exercício.

- 8. O aluno deverá ser capaz de explicar o funcionamento das principais linhas do seu código.

## Como salvar

Crie uma pasta com o seguinte formato:

Lista01_NomeDoAluno

Exemplo:

Lista01_AnaPaulaDoO

Dentro da pasta, salve os exercícios:

01_nome.py 02_idade.py 03_soma.py 04_media.py ... 20_desafio.py


## PARTE 1 — ENTRADA DE DADOS E VARIÁVEIS

## Questão 01 — Apresentação

Faça um programa que peça:

• nome;

- idade.

Depois, mostre uma mensagem apresentando a pessoa.

## Exemplo:

```
Digite seu nome: Ana
Digite sua idade: 25
Olá, Ana!
Você tem 25 anos.
```

## Questão 02 — Soma de dois números

Peça dois números inteiros ao usuário.

Depois, mostre a soma dos dois números.

## Exemplo:

```
Digite o primeiro número: 10
Digite o segundo número: 5
Soma = 15
```

## Questão 03 — Antecessor e sucessor

Peça um número inteiro.

## Mostre:

- o número digitado;

- seu antecessor;

- seu sucessor.

## Exemplo:


```
Digite um número: 10
Número: 10
Antecessor: 9
Sucessor: 11
```

## Questão 04 — Dobro

Peça um número inteiro e mostre o dobro desse número.

## Exemplo:

```
Digite um número: 8
O dobro é: 16
```

## Questão 05 — Média de duas notas

Peça duas notas de um aluno.

Calcule e mostre a média.

## Exemplo:

```
Digite a primeira nota: 8
Digite a segunda nota: 6
Média: 7
```

## PARTE 2 — DECISÕES: IF E ELSE

## Questão 06 — Maior de idade

Peça o nome e a idade de uma pessoa.

Se a idade for maior ou igual a 18, mostre:

```
Você é maior de idade.
```


Caso contrário:

Você é menor de idade.

## Questão 07 — Aprovado ou reprovado

Peça a média de um aluno.

Se a média for maior ou igual a 7, mostre:

Aluno aprovado.

Caso contrário:

Aluno reprovado.

## Questão 08 — Número positivo ou negativo

Peça um número inteiro.

Informe se ele é:

- positivo;

- negativo.

Desafio: pense também no que acontece quando o usuário digita 0 .

## Questão 09 — Maior número

Peça dois números inteiros.

Informe qual deles é maior.

## Exemplo:

Digite o primeiro número: 15

Digite o segundo número: 8

O primeiro número é maior.


## Questão 10 — Pode entrar?

Uma biblioteca permite a entrada de pessoas com idade igual ou superior a 12 anos.

Peça o nome e a idade da pessoa.

Informe:

Entrada permitida.

ou

Entrada não permitida.

## PARTE 3 — REPETIÇÃO COM FOR

## Questão 11 — Contagem

Faça um programa que mostre na tela os números de:

1 até 10

Utilize for e range() .

## Questão 12 — Contagem personalizada

Peça um número ao usuário.

Depois, mostre os números de 1 até o número informado.

## Exemplo:

Digite um número: 5

1

2

3

4

5


## Questão 13 — Tabuada

Peça um número ao usuário.

Mostre a tabuada desse número de 1 até 10.

## Exemplo:

```
Digite um número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

## Questão 14 — Contagem regressiva

Peça um número inteiro.

Mostre uma contagem regressiva desse número até 1.

## Exemplo:

```
Digite um número: 5
5
4
3
2
1
```

## Questão 15 — Números de 1 a 50

Faça um programa que mostre todos os números de 1 até 50.

```
Utilize for .
```

Desafio: modifique o programa para mostrar somente os números pares.


## PARTE 4 — OPERADOR %

## Questão 16 — Par ou ímpar

Peça um número inteiro.

Utilizando o operador % , informe se o número é:

PAR

ou

ÍMPAR

## Questão 17 — Pares de 1 a 20

Faça um programa que percorra os números de 1 até 20.

Mostre somente os números pares.

## Resultado esperado:

2

4

6

8

10

12

14

16

18

20

## Questão 18 — Divisível por 5

Peça um número inteiro.

Verifique se ele é divisível por 5.

## Dica:

Utilize o operador % .


Se:

numero % 5 == 0

o número é divisível por 5.

## PARTE 5 — STRINGS

## Questão 19 — Verificando uma palavra

Peça uma palavra ao usuário.

Depois, verifique se ela é igual à palavra:

python

Se for igual, mostre:

Você digitou Python!

Caso contrário:

Você digitou outra palavra.

## QUESTÃO 20 — DESAFIO FINAL

Faça um programa que peça:

- nome do aluno;

- idade;

- nota.

O programa deverá mostrar os dados informados.

Depois:

1. verificar se o aluno é maior ou menor de idade; 2. verificar se foi aprovado ou reprovado.

Considere:


```
Nota maior ou igual a 7 → Aprovado
Nota menor que 7 → Reprovado
```

## Exemplo

```
Digite seu nome: João
Digite sua idade: 20
Digite sua nota: 8
Nome: João
Idade: 20
Situação: Maior de idade
Resultado: Aprovado
```

## PARTE EXTRA — EXPLIQUE SEU CÓDIGO

Escolha 3 exercícios da lista.

Em cada um, escreva como comentário no próprio código uma explicação simples de pelo menos 3 linhas, explicando o que o programa faz.

## Exemplo:

```
\# Primeiro peço um número ao usuário.
# Depois verifico se o número é par.
# Por fim, mostro o resultado na tela.
```

## CRITÉRIOS DE AVALIAÇÃO


## ATENÇÃO

O aluno deverá conseguir explicar o próprio código.

Durante a aula, o professor poderá escolher qualquer exercício e solicitar:

- explicar uma determinada linha;

- alterar um número;

- alterar uma condição;

- modificar uma mensagem;

- executar o programa;

- corrigir um erro propositalmente inserido pelo professor.

A capacidade de explicar e modificar o próprio código fará parte da avaliação.
