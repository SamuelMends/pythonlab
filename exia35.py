# Crie um arquivo .py com duas funções 
# Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
# Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
# Importar o arquivo criado no Google Colab e testar as funções


def leitura():
    msg = str(input('Digite uma mensagem: '))
    return msg


def ler():
    num = float(input('Digite um número: '))
    return num


def resultado(msg,num):
    print(f'A mensagem digitada foi {msg} \nE o número digitado foi {num}')


msg = leitura()
num = ler()
resultado(msg,num)