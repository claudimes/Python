print('============== Exercicio 05 ==============')
numero = int(input('Digite um Numero: '))
resto = numero % 10
if resto ==0:
    print('A metade do número {} é'.format(numero), numero / 2)
else:
    print('O número digitado não termina com 0')
