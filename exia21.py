# Leia a idade do usuário e classifique-o em:
# Criança = 0 até 12 anos
# Adolescente = 13 até 17 anos
# Adulto = 18 anos (mostrar mensagem se o número for negativo)

def leitura():
    v = int(input('Digite sua idade: '))
    return v


def condition(v):
    if v < 0:
        print('Valores negativos')
    elif v < 13:
        print(f'Faixa Etária: CRIANÇA \nIdade {v} anos')
    elif v <= 17:
        print(f'Faixa Etária: ADOLESNCENTE \nIdade {v} anos')
    elif v >= 18:
        print(f'Faixa Etária: ADULTO \nIdade {v} anos')
    return v


v = leitura()
condition(v)