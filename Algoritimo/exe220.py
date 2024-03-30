print('============== Exercicio 20 ==============')
n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))
soma = n1 + n2
if soma < 8:
    print("A Media dos Numeros Informados é {:.2f}.".format(soma / 2))
else:
    if soma == 8:
        print('O Produto dos Numeros Informados é {}.'.format(n1 * n2))
    else:
        if soma > 8:
            if n1 > n2:
                print('A Divisão dos Numeros Informados é {:.2f}.'.format(n1 / n2))
            else:
                print('A Divisão dos Numeros Informados é {:.2f}.'.format(n2 / n1))



