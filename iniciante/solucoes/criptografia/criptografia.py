from math import ceil

n = int(input())
for i in range(n):
    msg = str(input())
#Para cada modificação em 'msg', cria-se uma nova string
#Primeiro passo
    msg2 = ''
    for x in msg:
        if (x.isalpha() == True):
            msg2 += chr(ord(x) + 3)
        else:
            msg2 += x
#Segundo passo
    msg3 = msg2[::-1]
#Terceiro passo
    s = ceil(len(msg3)/2)
    msg4 = msg3[-s:]
    msg5 = ''
    for y in msg4:
        msg5 += chr(ord(y) - 1)
    emsg = msg3.replace(msg4, msg5)
    print(emsg)