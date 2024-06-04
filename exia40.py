#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
"""
resp = float(input('Digite uma nota entre 0 e 10: '))
while resp > 10:
    print('Número incorreto! Digite um valor válido! ')
    resp = float(input('Digite uma nota entre 0 e 10 novamente: '))
    if resp <= 10:
        print(f'Está é sua nota {resp}')
        break 
"""

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

login = str(input('Digite seu login: '))
senha = input('Digite sua senha: ')

while senha == login:
    print('Senha incorreta!')
    senha = input('Digite sua senha novamente: ')
    if senha != login:
        print('Seja bem-vindo!')
        break