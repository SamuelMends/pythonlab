#Criando um contador sem limites:

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e eles possuem o tamanho de {tam} números!')


contador(2, 1, 7)
contador(3, 8, 4, 7, 9, 10)
contador(4, 4, 7, 9)