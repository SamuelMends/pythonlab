#Criando funções de Leitura, Soma e Resultado:

v1 = 0
v2 = 0

def leitura():
    print('Digite o primeiro valor: ')
    global v1
    v1 = int(input())
    print('Digite o segundo valor: ')
    global v2
    v2 = int(input())


def somatorio():
    global soma
    soma = v1 + v2


def resultado():
    print(f'Soma: {soma}')


leitura()
somatorio()
resultado()