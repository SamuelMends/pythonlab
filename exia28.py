# Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# Se a média for maior ou igual 0.0 e menor ou igual 4.0, o aluno está reprovado
# Se a média for maior que 4.0 e menor do que 6.0, o aluno pegou exame
# Se a média for maior ou igual a 6.0, o aluno está aprovado
# Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

def leitura():
    a = int(input('Digite sua nota N1: '))
    b = int(input('Digite sua nota N2: '))
    c = int(input('Digite sua nota N3: '))
    return a, b, c


def calculo(a,b,c):
    return (a+b+c)/3


def condition(med,exa):
    if med <= 4:
        print(f'Reprovado! média: {med:.2f}')
    elif med <=6:
        print(f'Exame! média: {med:.2f}')
        exa = float(input('Digite a nota do exame: '))
        if exa >= 6:
            print(f'Aprovado no exame! Média: {exa:.2f}')
        else:
            print(f'Reprovado! Média: {exa:.2f}')
    elif med >= 6:
        print(f'Aprovado! Média: {med:.2f}')
    return med, exa


a, b, c  = leitura()
med = calculo(a,b,c)
exa = None
condition(med,exa)