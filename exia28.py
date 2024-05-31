# Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# Se a média for maior ou igual 0.0 e menor ou igual 4.0, o aluno está reprovado
# Se a média for maior que 4.0 e menor do que 6.0, o aluno pegou exame
# Se a média for maior ou igual a 6.0, o aluno está aprovado
# Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

def leitura():
    n1 = int(input('Digite sua nota N1: '))
    n2 = int(input('Digite sua nota N2: '))
    n3 = int(input('Digite sua nota N3: '))
    return n1, n2, n3


def calculo():
    


def condition(n):
    if n <= 12:
        print(f'Faixa etária CRIANÇA, idade: {n}')
    elif n <=17:
        print(f'Faixa etária ADOLESCENTE, idade: {n}')
    elif n >= 18:
        print(f'Faixa etária ADULTO, idade: {n}')
    return n 


i = leitura()
condition(i)