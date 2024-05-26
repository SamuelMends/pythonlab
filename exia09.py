#Importando Numpy:
import numpy
#Estabelecendo Vetor de 5 slots:
vetor = numpy.empty(5)
#Criando laço de repetição para armazenar dados nos 5 slots:
for c in range(0,5):  
#Adicionando os valores dos 5 slots de memória na variável VALOR:  
    valor = float(input(f'Digite o valor {c+1}: '))
#Adcionando os valores da Variável valor nos 5 slots do vetor:
    vetor[c] = valor
#Criando um novo laço para mostrar os valores do 5 slots:
for c in range(0,5):
    print(vetor[c])
