'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''


login = str(input('Digite seu login: '))
senha = str(input('Digite sua senha: '))

while login == senha:
    print('Credenciais incorretas! Por gentileza, tente novamente: ')
    login = str(input('Digite seu login: '))
    senha = int(input('Digite sua senha: '))
print('Login realizado com sucesso!')