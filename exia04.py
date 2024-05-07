#Apresentar o quadrado dos npumeros inteiros de 15 a 200 (CONTADOR)
#Exia04


cont = 1
num = int(input('Digite um número inteiro entre 15 e 200: '))
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

