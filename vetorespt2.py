#Importando Numpy
import numpy

vetor = numpy.empty(5)
for position in range (0,5):
    vetor[position]= int(input(f'Digite o {position+1}º valor: '))
pesquisa = int(input('Digite o valor a ser pesquisado: '))
for position in range (0,5):
    if vetor[position] == pesquisa:
        print(f'Valores encontrados na posição {position+1}º')
   
