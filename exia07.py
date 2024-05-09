'''
Ler duas notas e informar a média, Se o valor digitado for menor do que 0 ou maior do que 10, o usuario deve digitar a nota novamente, 
'''

nota1 = float(input('Digite sua primeira nota: '))
while nota1 < 0 or nota1 > 10:
  print('Valores incorretos!')
  nota1 = float(input('Digite sua primeira nota novamente: '))
nota2 = float(input('Digite sua segunda nota: '))
while nota2 < 0 or nota2 > 10:
  print('Valores incorretos!')
  nota2 = float(input('Digite sua primeira nota novamente: '))
med = (nota1+nota2)/2
print(f'A sua média é de {med}')