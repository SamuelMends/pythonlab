nota1 = float(input('Digite sua em português: '))
nota2 = float(input('Digite sua em matemática: '))
nota3 = float(input('Digite sua história: '))
med = (nota1 + nota2 + nota3)/3
if med > 8:
    print('Parabéns você foi aprovado! Sua média foi de {:.2f}'.format(med))
elif med < 8 and med > 4:
    print('Você ficou de recuperação pois sua média foi de {:.2f}'.format(med))
elif med < 4:
    print('Infelizmente você não passou sua média foi de {:.2f}'.format(med))
print('Até a próxima!')
