# Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

lista = [] #Lista Vazia sem variáveis
for num in range(1,6): #Adicionamos o range de 5 repetições
    n = int(input(f'Digite o {num}º número: ')) #Fazendo a pergunta 5x
    lista.append(n) #Usamos o Append para adicionar o elemento em uma lista
print(lista)    


# Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

