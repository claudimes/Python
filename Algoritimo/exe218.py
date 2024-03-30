print('============== Exercicio 18 ==============')
n1 = float(input('Digite o Primeiro Numero: '))
n2 = float(input('Digite o Segundo Numero: '))
codigo = int(input('Digite o Codigo: '))
if codigo == 1:
    print(f'A Soma dos Numeros Digitados é:  {n1 + n2:.2f}')
else:
    if codigo == 2:
        print(f'A Soma dos Numeros Digitados é:  {n1 * n2:.2f}')
    else:
        if codigo == 3:
            print(f'A Soma dos Numeros Digitados é:  {n1 / n2:.2f}')
        else:
            print('Código inválido!')