print('Gerador de P.A')
print('-='*20)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{} >'.format(termo), end =' ')
    termo += razao
    cont += 1    
print('Pausa')
print('Quantos termos você quer mostrar a mais?')
    