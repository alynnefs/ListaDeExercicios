def hasSum(lista, sum_number):
    diff = []
    for number in lista:
        if lista.contains(sum_number):
            return True
        diff.append(sum_number-number)
    return False


list = [ 4, 1, 7, 3, 8, 3]
print(list, 6)