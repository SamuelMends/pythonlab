'''
Apresente o total da soma obtida dos cem primeiros número inteiros de 1 até 100 (Acumulador)
'''
#EXIA05:

#for c in range (0,100,):
   # cont = c + 1
    #soma = c + c
    #results = soma + soma
    #print(f'Somatório dos 100 primeiros números é {results}')
    #print(f'A soma de {c} + {cont} é de {soma + 1}')

contador = 1
soma = 0
while contador <=100:
    soma = soma + contador
    contador += 1
    print(f'Somatório dos 100 primeiros números: {soma}')