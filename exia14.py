#Leia uma matriz 4x4 e apresente:
#A) - O somatório da segunda linha da matriz: DONE!
#B) - O somatório da segunda coluna da matriz:
#C) - O somatório de todos os elementos da matriz:


import numpy
matriz = numpy.empty([4,4])
for linha in range(0,4):
    for coluna in range(0,4):
        data = int(input(f'Digite o valor referente a linha {linha} e a coluna {coluna}: '))
        matriz[linha][coluna] = data
        somalinha = matriz[2][0]+matriz[2][1]+matriz[2][2]+matriz[2][3]
        somacoluna = matriz[0][2]+matriz[1][2]+matriz[2][2]+matriz[3][2]
        somatotal = numpy.sum(matriz)
print(f'O somatório da segunda linha possui o total de {somalinha}')
print(f'O somatório da segunda coluna possui o total de {somacoluna}')
print(f'O somatório total da matriz é de {somatotal}')