#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#Números
#CEPs
#URLs

import re

frase = 'Olá, meu CEP é de telefone é 13185-541'

resultado = re.search('\d{0,5}-\d{0,4}', frase)
if resultado:
    print("CEP Encontrado:", resultado.group())
else:
    print("Número de telefone não encontrado.")


# frase = 'Olá, meu CEP é 13185-541'


# CEP 12345-000