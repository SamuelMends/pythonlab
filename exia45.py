# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for c in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

media = sum(numeros) / len(numeros)
soma = sum(numeros)

print(f'A soma dos números é igual a {soma}\nE a sua média {media}')