#Código Práctica 1
#Código Práctica 1

import sys

numero = int(sys.argv[1]) + 1

def lista(numero):
    
    lis = []
    
    for i in range (1,numero):
        lis.append(i)
    return lis


def primo(numero):
    lis2 = []
    
    for i in lista(numero):
        if numero % i  == 0:
            lis2.append(numero)
    return lis2
    


print(primo(numero))



    

    