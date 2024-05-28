#Criando a função soma
"""
def soma(a,b):
    print(f'A soma de A = {a} + B = {b}')
    s = a+b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
"""

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e eles possuem o tamanho de {tam} números!')


contador(2, 1, 7)
contador(3, 8, 4, 7, 9, 10)
contador(4, 4, 7, 9)
