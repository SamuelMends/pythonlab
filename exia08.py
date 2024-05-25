'''
Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma caixa retangular. Utilize para cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA. Ao final do cálculo, perguntar ao usuário se deseja continuar o programa fazendo nova leitura 
'''

print('-'*20)
print('Valores de comprimento!')
print('-'*20)
comp = float(input('Digite o comprimento: '))
larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
vol = (comp * larg * alt)
print(f'O volume é de {vol}')
resp = str(input('Deseja fazer uma nova leitura [S/N]: '))
while resp == 'S':
    print('-'*20)
    print('Valores de comprimento!')
    print('-'*20)
    comp = float(input('Digite o comprimento: '))
    larg = float(input('Digite a largura: '))
    alt = float(input('Digite a altura: '))
    vol = (comp * larg * alt)
    print(f'O volume é de {vol}')
    resp = str(input('Deseja fazer uma nova leitura [S/N]: '))
print('Programa finalizado!')