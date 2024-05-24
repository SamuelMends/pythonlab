nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
med = (nota1 + nota2)/2
if med > 4:
    print(f'Parabéns você foi aprovado! Sua média foi de {med}')
else:
    print(f'Infelizmente você não passou sua média foi de {med}')
print('Até a próxima!')
