'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

nota = int(input('Digite sua nota: '))

while nota < 0 or nota > 10:
    print('Este valor é inválido!')
    nota = int(input('Digite sua nota novamente: '))
print('Sua nota é {} fim'.format(nota))