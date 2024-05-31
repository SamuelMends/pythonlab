# Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução

# Leia a idade do usuário e classifique-o em:
# Criança – 0 a 12 anos
# Adolescente – 13 a 17 anos
# Adulto – acima de 18 anos
# Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

def leitura():
    i = int(input('Digite sua idade: '))
    return i


def condition(i):
    if i <= 12:
        print(f'Faixa etária CRIANÇA, idade: {i}')
    elif i <=17:
        print(f'Faixa etária ADOLESCENTE, idade: {i}')
    elif i >= 18:
        print(f'Faixa etária ADULTO, idade: {i}')
    return i 


i = leitura()
condition(i)