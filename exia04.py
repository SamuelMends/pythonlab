#Apresentar o quadrado dos npumeros inteiros de 15 a 200
'''
num = int(input('Digite um número inteiro: '))
while num < 15 or num > 200:
    print('Número inválido!')
    num = int(input('Digite um número inteiro novamente: '))
cal = (num * num)
print(f'O quadrado desse número é {cal}')
'''




for num in range (15,201,):
    print(f'O resultado do quadrado de {num} é igual a {num*num}')
        