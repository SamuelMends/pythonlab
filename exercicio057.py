
sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invávlidos, digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo)) 