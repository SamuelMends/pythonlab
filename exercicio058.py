from random import randint
from time import sleep
print('Sou seu computador...')
sleep(1)
pcchoice = randint(1,10)
print('Acabei de pensar em um número entre 0 e 10')
sleep(1)
print('Será que você consegue advinhar qual foi? ')
sleep(1)
palpit = int(input('Qual o seu palpite? '))
while palpit != pcchoice:
    palpit = int(input('Não foi nesse número que eu pensei... tente novamente: '))
    if palpit > pcchoice:
        print('Meu número foi mais baixo, tente novmente: ')
    elif palpit < pcchoice:
        print('Meu número foi mais alto tente novmente: ')
else: palpit == pcchoice
print('Parabéns você acertou')
print('Fim')