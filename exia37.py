# Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
# Cada aluno deve ocupar uma linha do novo arquivo de texto
# O formato deve ser: nome,nota (Pedro,8.0)
# Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
"""
with open('file.txt', 'w') as texto:
    for element in alunos:
        texto.write(element)
        print(texto)
"""
"""
#Código pra alterar o conteúdo:
with open('file.txt', 'w') as texto:
    texto.write('EU SOU O SAM DEV')
    print(texto)
"""
"""
#Código pra ver o conteúdo:
with open('file.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
""" 

# Gravando os alunos em um novo arquivo de texto
with open('alunos.txt', 'w') as arquivo:
    for nome, nota in alunos.items():
        arquivo.write(f"{nome},{nota}\n")

# Lendo o arquivo e mostrando todos os alunos
with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(',')
        print(f"Nome: {nome}, Nota: {nota}")

# Este código faz o seguinte:

   # Abre um novo arquivo chamado 'alunos.txt' para escrita ('w').
   # Itera sobre cada elemento do dicionário alunos, gravando o nome do aluno e sua nota no formato especificado em uma linha do arquivo.
   # Fecha o arquivo após a conclusão da gravação.
   # Abre o arquivo 'alunos.txt' para leitura ('r').
   # Itera sobre cada linha do arquivo, dividindo-a em nome e nota usando a função split().
   # Imprime o nome e a nota de cada aluno.
