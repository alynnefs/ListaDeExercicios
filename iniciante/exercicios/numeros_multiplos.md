# Números múltiplos
Utilizando a linguagem de programação Python, crie uma função que encontre os múltiplos de um número qualquer até um determinado limite
oferecido pelo usuário.
A função deverá ter como entrada dois números. Um deles será o limite, e o outro deverá ser o múltiplo.
A função deve retornar como saída uma lista contendo os múltiplos.

### Regras
1. Caso o múltiplo dado pelo usuário seja 0, a função deverá retornar somente uma lista contendo um único elemento, o 0.
2. Caso o múltiplo dado pelo usuário seja negativo, a função deverá retornar uma mensagem de erro indicando que o número é inválido.

### Exemplo
Considere a função abaixo como exemplo:
```
Multiplos(múltiplo, limite)
```
Utilizando a função acima para encontrar os múltiplos de 5 até o número 50, obteremos o seguinte resultado:
```
Multiplos(5, 50)

Múltiplos de 5: 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
```

### Exercício
Como exercício, encontre os múltiplos de 4 e 7 até o número 90.

### Gabarito
```
Múltiplos de 4: 1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88
Múltiplos de 7: 1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84
```