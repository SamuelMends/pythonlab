#Leia dois números inteiros e informe qual deles é o maior. Se os npumeros forem iguais
#mostrar esta informação na tela:
#Exia3

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é o maior')
elif num1 == num2:
    print('Os números são iguais')
    