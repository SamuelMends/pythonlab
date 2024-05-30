# Crie um programa que leia três valores e calcule a média aritmética dos valores lidos
# Função para ler os valores (não recebe parâmetro e retorna valor lido)
# Função para calcular a média (recebe como parâmetro os três valores e retorna o resultado)
# Função para mostrar o resultado (recebe como parâmetro o valor da média e imprime o valor, não retorna nada)

def leitura():
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    n3 = int(input('Digite o terceiro valor: '))
    return n1,n2,n3


def calculo(n1,n2,n3):
    return (n1 + n2 + n3) / 3
    


def resultado(s):
    print(f'A média aritmética dos 3 valores é de {s}')


n1,n2,n3 = leitura()
s = calculo(n1,n2,n3)
resultado(s)