# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
# e C é a temperatura em graus Celsius

# Função para ler os valores:
# Função para fazer o cálculo:
# Função para mostrar o resultado:

def leitura():
    grau = float(input('Digite os graus em Cº: '))
    return grau


def calculo(grau): #Função para calcular os graus
    return (9 * grau + 160) / 5


def resultado(cal):
    print(f'Os graus passados em Cº equivalem em Fº {cal}')


grau = leitura() #Nossa função leitura irá receber a variavel "Grau".
cal = calculo(grau) #Precisamos apenas passar a variavel "Grau" pois nossa função 'calculo' já calcula.
resultado(cal) #Precisamos apenas passar o resultado "Cal".

