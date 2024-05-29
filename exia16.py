#Crie uma função que imprima na tela a palavra "Programação" 10 vezes:


def prog():
    print('\nProgramação'*10)


prog()

cont = 1

for program in range(0,10):
    cont +=1
    print(f'Programação {cont-1}º')