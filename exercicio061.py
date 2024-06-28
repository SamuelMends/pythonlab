print('Gerador de P.A') #Nosso gerador de PA
print('-='*20)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{} >'.format(termo), end =' ')
    termo += razao
    cont += 1
print('Fim')