#Criando funções de Leitura, Soma e Resultado:

def leitura():
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    return v1, v2

def somatorio(v1, v2):
    return v1 + v2

def resultado(soma):
    print(f'Soma: {soma}')

# Chama as funções em sequência
v1, v2 = leitura()
soma = somatorio(v1, v2)
resultado(soma)
