'''
Escreva um algoritimo que lê 5 valores para a variável A, um de cada vez, e conta quantos destes valores são negativos. Após a leitura, o programa deve mostrar a quantidade de números negativos
'''
#Exia 06:

cont = 0
for c in range (0,5,):
    num = int(input('Digite um número: '))
    if num < 0:
        cont +=1  
print(f'O total de números negativos foi de {cont}')
