# Leia um número inteiro e informe e retorne se ele é positivo 
# Função para ler o valor (não recebe parâmetro e retorna o valor lido)
# Função para postivo (recebe como parâmetro o valor lido retorna verdadeiro se for positivo ou falso se for negativo)


def leitura():
    v = int(input('Digite o valor: '))
    return v


def condition(v):
    if v < 0:
        print(f'Número {v} é negativo')
    else:
        print(f'Número {v} é positivo')


v = leitura()
condition(v)