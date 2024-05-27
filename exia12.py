#Leia um vetor de 10 elementos e apresente:
#A) - O somatório de todos os valores: DONE!
#B) - A média de todos os valores: DONE!
#C) - A quantidade de numeros negativos: DONE!

import numpy
cont = 0
med = 0
neg = 0
vetor = numpy.empty(10)
for c in range(0,10):
    p = int(input(f'Digite o {c+1}º valor: '))
    vetor [c] = p
    cont = p + cont
    med = cont/10
    if p < 0:
        neg += 1
print(f'O somatório de todos os valores é igual a {cont}')
print(f'A média de todos os valores é igual a {med}')
print(f'O total de números negativos digitados é de {neg}')