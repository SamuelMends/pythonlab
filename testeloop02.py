'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).

'''


nome = str(input('Nome: '))
while len(nome) < 3:
    print('Por favor digite mais caracteres: ')
    nome = str(input('Nome: '))
idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    print('Idade inválida!') 
    idade = int(input('Digite a idade novamente: '))
salario = float(input('Salário: '))
while salario < 0:
    print('Valores inválidos!')
    salario = float(input('Digite o salário novamente: '))
sexo = str(input('M ou F: '))
while sexo not in 'M'and 'F':
    print('Valores inválidos!')
    sexo = str(input('Digite seu sexo novamente M ou F: '))
estadocivil = str(input('Estado civil [S]: '))


