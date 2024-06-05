#Faça um programa que leia 5 números e informe o maior número. 

import numpy as np

numeros = []

for c in range(1,6):
    num = int(input('Digite um número: '))
    numeros.append(num)

maior = max(numeros)

print(f'O maior número é {maior}')


