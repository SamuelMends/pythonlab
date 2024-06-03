#1) Crie uma classe chamada aluno com os seguintes atributos:
# Nome:
# Nota 01:
# Nota 02:
# Crie um construtor para a classe (__init__)
#2) Crie as seguintes funções (métodos):
# Calcula média, retornando a média aritmética entre as notas
# Mostra dados, que somente imprime o valor de todos os atributos
# Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
#3) Crie dois objetos (aluno1 e aluno2) e teste as funções


class alunos:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    

    def med(self):
        return (self.nota1 + self.nota2) / 2
    

    def total(self):
        return (self.nota1 + self.nota2)
    
    def resultado(self):
        if self.med() >= 6.0:
            print(f'O Aluno {self.nome} está aprovado com média {self.med()}')
        else:
            print(f'Aluno {self.nome} reprovado.')


a1 = alunos("Samuel", 10, 10)

print('Média geral', a1.med())
a1.resultado()
print('Pontos Totais', a1.total())

a2 = alunos("Pedro", 3, 8)

print('Média geral', a2.med())
a2.resultado()
print('Pontos Totais', a2.total())

