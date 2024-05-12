from math import factorial
num=int(input('Digite o seu número: '))
#C é o nosso contador:
c = num
#F é o nosso limite:
f = 1
while c > 0:
    print('{}'.format(c), end= '')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O seu número foi {} e seu fatorial é {}'.format(num,factorial(num)))
