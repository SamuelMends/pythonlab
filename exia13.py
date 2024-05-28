#Leia uma matriz de inteiros 3x3. Após leia um valor individual e mostre quantas vezes o número #digitado aparece na matriz

import numpy
matriz = numpy.empty([3,3])
for linha in range (0,3):
    for coluna in range(0,3):
        data = int(input(f'Digite o valor da linha {linha} e da coluna {coluna}: '))
        matriz [linha][coluna] = data
pesq = int(input('Digite o valor individual: '))
q = 0
for linha in range (0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] == pesq:
            q += 1
print(f'Quantidade do valor é de {q} vezes')
