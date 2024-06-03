#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#Números
#CEPs
#URLs


#Números

import re

numero = 'Olá, meu CEP é de telefone é (19)99350-9699'

resultado = re.search('\(\d{2}\)\d{4,5}-\d{4}', numero)
if resultado:
    print("Número de telefone encontrado:", resultado.group())
else:
    print("Número de telefone não encontrado.")

# CEP 12345-000

cep = 'Olá, meu CEP é de telefone é 13185-541'

resultado = re.search('\d{0,5}-\d{0,4}', cep)
if resultado:
    print("CEP Encontrado:", resultado.group())
else:
    print("CEP não encontrado.")

#URL

url = 'Olá, meu URL é www.google.com'

resultado = re.search('\w+.\w+\.com', url)
if resultado:
    print("URL encontrada:", resultado.group())
else:
    print("URL não encontrada")