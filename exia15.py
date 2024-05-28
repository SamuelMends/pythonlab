#Leia duas matrizes A e B com as dimensões 3x3. Crie uma nova matriz C de mesma dimensão
#Que seja a soma de A + B. No final, imprimir a matriz C

import numpy
matriza = numpy.empty([3,3])
matrizb = numpy.empty([3,3])
matrizc = numpy.empty([3,3])
for linha in range(0,3):
    for coluna in range(0,3):
        dataa = int(input(f'Digite o valor referente a linha {linha} e a coluna {coluna}: '))
        matriza[linha][coluna] = dataa
for linha in range(0,3):
    for coluna in range(0,3):
        datab = int(input(f'Digite o valor referente a linha {linha} e a coluna {coluna}: '))
        matrizb[linha][coluna] = datab
matrizc[linha][coluna] = (numpy.sum(matriza))+(numpy.sum(matrizb))
print(matrizc[linha][coluna]) 