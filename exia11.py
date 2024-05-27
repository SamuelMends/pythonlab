#Leia um vetor A com 10 elementos do tipo real. Construir um vetor B de mesmo tipo, 
#Sendo que cada elemento do vetor B deve ser o cubo de cada elemento correspondente do vetor A
#Apresentar no final os dois vetores.

import numpy
vetora = numpy.empty(10)
vetorb = numpy.empty(10)
for m in range (0,10):
    q = int(input(f'Digite o {m+1}º valor: '))
    vetora[m] = q
cont = 1
for vetorb in range(0,10):
    vetorb = (vetora[m]**2)
print(f'O valor dos vetores do tipo A são {vetora} e seus respectivos quadrados {vetorb}')