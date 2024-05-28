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
        somalinha = matriz[2][0]+matriz[2][1]+ matriz[2][2]+matriz[2][3]
print(f'O somatório da segunda linha possui o total de {somalinha}')
print(f'O somatório da segunda coluna')
    