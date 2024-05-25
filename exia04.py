#Apresentar o quadrado dos npumeros inteiros de 15 a 200
'''
cont = 1
num = int(input('Digite um número inteiro: '))
while num < 15 or num > 200:
    print('Número inválido!')
    num = int(input('Digite um número inteiro novamente: '))
cal = (num * num)
print(f'O quadrado desse número é {cal}')

'''
'''
N = False
while resp == 'S':
    con = num + cont
    cal = (con * con)
    print(f'O quadrado do proximo número {con} número é {cal}')
print('Programa finalizado!')
'''
'''

for num in range (15,201,):
    print(f'O resultado do quadrado de {num} é igual a {num*num}'
'''


cont = 1
num = int(input('Digite um número inteiro: '))
while num < 15 or num > 200:
    print('Número inválido!')
    num = int(input('Digite um número inteiro novamente: '))
cal = num * num
print(f'O quadrado desse número é {cal}')

resp = input('Deseja continuar? [S/N]: ').upper()  # Convertendo para maiúsculas para facilitar a comparação

while resp == 'S':
    cont += 1
    prox_num = num + cont
    prox_cal = prox_num * prox_num
    print(f'O quadrado do próximo número {prox_num} é {prox_cal}')
    resp = input('Deseja continuar? [S/N]: ').upper()

print('Programa finalizado!')
