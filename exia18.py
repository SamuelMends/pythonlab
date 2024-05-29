# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula: DISTÂNCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade De litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem:

# Função para ler os valores:
# Função para calcular a distância:
# Função para calcular a quantidade de litros:
# Função para apresentar o resultado:

def ler():
    t = float(input('Digite o tempo gasto na viagem: '))
    v = float(input('Digite a velocidade média: '))
    return t, v


def calculo(t,v):
    return t*v


def calculin(t,v):
    return (t*v)/12


def resultado(v,t,d,lus):
    print(f'O valor da velocidade média é de {v}, o tempo gasto foi de {t}, a distância percorrida foi de {d:.2f} e a quantidade de litros de {lus:.2f}')


t, v = ler()
d = calculo(t,v)
lus = calculin(t,v)
resultado (v,t,d,lus)
