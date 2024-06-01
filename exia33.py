# Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

alunos = {} #Criando dicionário
for a in range(1,4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota #Para adicionar um elemento no dicionário: acessamos colocamos colchetes
print(alunos)
print(alunos['maria'])