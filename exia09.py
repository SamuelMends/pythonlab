#Leia um vetor A de 10 elementos inteiros e um valor individual X.
#A seguir, imprimir os índices do vetor A em que aparece um valor igual a X:

import numpy
vetor = numpy.empty(10)
for a in range(0,10):
    data = int(input(f'Digite o valor {a+1}º: '))
    vetor[a] = data
pesq = int(input('Digite o valor de pesquisa: '))
for a in range(0,10):
    if vetor[a] == pesq:
        print(f'Valor encontrado na posição {a+1}º')