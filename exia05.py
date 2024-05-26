'''
Apresente o total da soma obtida dos cem primeiros número inteiros de 1 até 100
'''

for c in range (0,100,):
    cont = c + 1
    soma = c + c
    results = soma + soma
    print(f'Somatório dos 100 primeiros números é {results}')
    #print(f'A soma de {c} + {cont} é de {soma + 1}')