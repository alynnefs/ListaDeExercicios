## Enunciado do exercício.
Analisando a conjectura de Collatz
Você está resolvendo este problema.
Este problema foi utilizado em 223 Dojo(s).
Para definir uma sequência a partir de um número inteiro o positivo, temos as seguintes regras:
```
n → n / 2 (se n é par)
n → 3n + 1 (se n é ímpar)
```
Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
```
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

```
Podemos ver que esta sequência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a sequência resultante chega no número 1 em algum momento.
Desenvolva um programa que dado um número x  produza sua sequência de Collatz.
