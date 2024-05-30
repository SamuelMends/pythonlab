# Leia um número inteiro e informe se ele é positivo ou negativo
# 1 Função para ler o número inteiro (recebe uma mensagem)
# 2 Função para apresentar se é positivo ou negativo, recebendo como parâmetro o número lido:


def leitura():
    v = int(input('Digite um valor: '))
    return v


def verificar(v):
    if v < 0:
        print(f'O número {v} é negativo')
    else:
        print(f'O número {v} é positivo')
    return v


v = leitura()
verificar(v)