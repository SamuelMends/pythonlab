import numpy

matriz = numpy.empty([2, 2])
matriz[0][0] = 3
matriz[0][1] = 6
matriz[1][0] = 9
matriz[1][1] = 21
print(matriz[1][0])

for linha in range(0,2):
    print(f'{linha}')
for coluna in range(0,2):
    print(f'{coluna}')
