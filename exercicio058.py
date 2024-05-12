from random import randint
from time import sleep
pcchoice = randint(1,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
sleep(1)
print('Será que você consegue advinhar qual foi? ')
acertou = False
tent = 0
while not acertou:
    palpit = int(input('Qual o seu palpite? '))
    tent += 1
    if palpit == pcchoice:
        acertou = True
    else:
        if palpit < pcchoice:
            print('Mais...Tente novamente: ')
        elif palpit > pcchoice:
            print('Menos...Tente novamente: ')
print('Parabéns você acertou com {} tentativas'.format(tent))
        