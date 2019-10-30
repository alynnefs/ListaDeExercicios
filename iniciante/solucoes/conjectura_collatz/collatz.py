def verifica_collatz(numero):
    if numero % 2 != 0:
        return (numero * 3) + 1
    return numero // 2


def sequencia_de_collatz(numero):
    sequencia = [numero]
    novo_numero = numero
    while novo_numero != 1:
        novo_numero = verifica_collatz(novo_numero)
        sequencia.append(novo_numero)
    return sequencia


def calcula_tamanho_da_sequencia_de_collatz(numero):
    return len(sequencia_de_collatz(numero))
