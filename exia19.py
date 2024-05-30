# Ler os valores de comprimento, largura e altura e apresentar o valor do volume de uma caixa retangular. Utilize para o cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA

def leitura():
    c = float(input('Digite o valor de comprimento: '))
    l = float(input('Digite o valor de largura: '))
    a = float(input('Digite a altura: '))
    return c,l,a


def calculo(c,l,a):
    return c*l*a


def resultado(v,c,l,a):
    print(f'Possuindo os seguintes parametros: \nComprimento {c}\nLargura {l}\nAltura {a}\nNosso volume é de {v}')



c,l,a = leitura()
v = calculo(c,l,a)
resultado(v,c,l,a)
