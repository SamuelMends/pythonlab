#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#Números
#CEPs
#URLs

import re

frase = 'Olá, meu CEP é de telefone é (42)0000-0000'

resultado = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
if resultado:
    print("Número de telefone encontrado:", resultado.group())
else:
    print("Número de telefone não encontrado.")


frase = 'Olá, meu CEP é de telefone é 13185-541'

resultado = re.search('\d{0,5}-\d{0,4}', frase)
if resultado:
    print("CEP Encontrado:", resultado.group())
else:
    print("CEP não encontrado.")


# CEP 12345-000