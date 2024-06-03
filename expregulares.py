import re

frase = 'Olá, meu número de telefone é (42)0000-0000'

resultado = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
if resultado:
    print("Número de telefone encontrado:", resultado.group())
else:
    print("Número de telefone não encontrado.")