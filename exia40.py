#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

resp = float(input('Digite uma nota entre 0 e 10: '))
while resp > 10:
    print('Número incorreto! Digite um valor válido! ')
    resp = float(input('Digite uma nota entre 0 e 10 novamente: '))
    if resp <= 10:
        print(f'Está é sua nota {resp}')
        break 


