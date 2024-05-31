# Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução. Implemente cada exercício utilizando tanto o for quanto o while

# Ler 5 notas e informar a média
# Imprimir a tabuada do número 3 (3 x 1 = 1 – 3 x 10 = 30)

nota = media = soma = 0

for n in range(5):
    n1 = int(input(f'Digite sua nota {n+1}: '))
    soma = soma + n1
med = (soma)/5
print(f'Sua média é igual a {med}')


"""
notas = []

for n in range(5):
    nota = int(input(f'Digite sua nota {n+1}: '))
    notas.append(nota)

med = sum(notas) / len(notas)
print(f'Sua média é igual a {med}')
"""
som = 0
cont = 0 
while cont < 5:
    nota = int(input(f'Digite sua {cont+1}º nota: '))
    som += nota
    cont +=1
med = som/5
print(f'Sua média é igual a {med}')