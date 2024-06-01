#Código pra ver o conteúdo:


#Neste exemplo:

    #'arquivo.txt' é o nome do arquivo que você deseja abrir. Certifique-se de que ele esteja no mesmo diretório do seu script Python ou forneça o caminho completo para o arquivo.
    #'r' indica que o arquivo será aberto em modo de leitura. Se o arquivo não existir, isso levantará um erro. Se você deseja criar um novo arquivo se ele não existir, use 'w' (modo de escrita).
    #as arquivo atribui o objeto de arquivo retornado pela função open() a uma variável chamada arquivo.
    #arquivo.read() lê todo o conteúdo do arquivo e o armazena na variável conteudo.
    #print(conteudo) imprime o conteúdo do arquivo.

#Após abrir o arquivo usando open(), é uma boa prática usar o bloco with para garantir que o arquivo seja fechado corretamente após o uso, mesmo se ocorrerem exceções durante a execução do código. O bloco with cuida do fechamento do arquivo automaticamente quando você sai do bloco.

#Código pra alterar o conteúdo:
with open('file.txt', 'w') as texto:
    texto.write('EU SOU O SAM DEV')
    print(texto)

#Código pra ver o conteúdo:
with open('file.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)