#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

login = str(input('Digite seu login: '))
senha = input('Digite sua senha: ')

while senha == login:
    print('Senha incorreta!')
    senha = input('Digite sua senha novamente: ')
    if senha != login:
        print('Seja bem-vindo!')
        break