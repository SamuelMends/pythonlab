primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Qual sua opção? '))
if opcao == 5:
        print('-'* 20)
        print('Finalizando...')
        print('-'* 20)
elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
elif opcao == 3:
        if primeiro > segundo:
                print('O primeiro número é maior do que o segundo.')
        else:
                print('O segundo número é maior!')
elif opcao == 2:
        calculom = primeiro * segundo
        print('O valor da multiplicação entre {} e {} é de {}'.format(primeiro,segundo,calculom))
elif opcao == 1:
        calculos = primeiro + segundo
        print('O valor da soma entre {} e {} é de {}'.format(primeiro,segundo,calculos))