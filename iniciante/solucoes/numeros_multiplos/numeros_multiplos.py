# Função que soluciona o problema

def Multiplos(multiplo, limite):
    auxiliar = 1
    multiplicador = 1
    listaMultiplos = []

    if(multiplo < 0):
        return 'Erro: número menor que 0!'

    if(multiplo == 0):
        listaMultiplos.append(0)
        return listaMultiplos

    if(limite >= 1):
        listaMultiplos.append(1)

    while(auxiliar <= limite):
        auxiliar = multiplicador * multiplo
        if(auxiliar <= limite):
            listaMultiplos.append(auxiliar)
        multiplicador += 1

    return listaMultiplos

# Entrada
limite = int(input('Número limite: '))
multiplo = int(input('Múltiplo: '))

resultado = Multiplos(multiplo, limite)

# Checa se o retorno foi uma string para imprimir a mensagem de erro
if(isinstance(resultado, str)):
    print(resultado)

# Imprime a saída
else:
    print('Múltiplos de ' + str(multiplo) + ': ' + str(resultado))