#Leia um vetor A de 10 elementos inteiros e um valor individual X.
#A seguir, imprimir "Achei" se o valor X existir em A e 'Não achei' caso contrário.

import numpy
vetor = numpy.empty(10)
for a in range(0,10):
    x = int(input(f'Digite o {a+1}º valor: '))
    vetor[a] = x
p = int(input('Digite o valor de pesquisa: '))
achei = False
for a in range(0,10):
    if vetor[a] == p and achei == False:
        print(f'Achei na posição {a+1}º')
    elif achei == True:
        print('Não achei')
