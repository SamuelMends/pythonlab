# Tratamento de erros e exceções

#  NameError: variável nao foi definida
#  TypeError: tipos de dados incompatíveis
#  RuntimeError: erro de execução
#  SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
#  ZeroDivisionError: divisão por zero
#  IndexError: índice está fora da coleção


# Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
# ValueError: se o usuário digitar um caracter
# ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# KeyboardInterrupt: caso o usuário interrompa a execução
# Mostre uma mensagem personalizada na ocorrência de cada um desses erros


import numpy as np

lista = []

while True:
  try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    resultado = lista[0]/lista[1]
  except ValueError:
    print('Valor inválido')
  except ZeroDivisionError:
    print('Usuário digitou Zero e ocorreu erro na divisão')
  except IndexError:
    print('Divisão sendo feita com números não inseridos não existem na lista')  
  except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
    break
  else:
    print(f'Valor da divisão é {resultado}')
    break