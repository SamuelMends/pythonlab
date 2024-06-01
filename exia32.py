# Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

lista = [] #Lista Vazia sem variáveis
for num in range(1,6): #Adicionamos o range de 5 repetições
    n = int(input(f'Digite o {num}º número: ')) #Fazendo a pergunta 5x
    lista.append(n) #Usamos o Append para adicionar o elemento em uma lista
print(lista)    

#Existem duas formas de fazer a soma, manual e automática

#Manual:
som = 0 
for c in range(len(lista)):
    som += lista[c]
print(f'Soma: {som}')

#Automatica:
import numpy as np #Importando o numpy e dando o nome de np
np.array(lista).sum() #Vamos converter a lista para o formato array e depois usar o sum para somar os valores de dentro da lista




