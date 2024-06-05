# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 


def calcula_anos(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0
    while populacao_a < populacao_b:
        populacao_a *= 1 + taxa_a / 100
        populacao_b *= 1 + taxa_b / 100
        anos += 1
    return anos

populacao_a = 80000
taxa_crescimento_a = 3
populacao_b = 200000
taxa_crescimento_b = 1.5

anos_necessarios = calcula_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)

print(f'Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.')
