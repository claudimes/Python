n = int(input('Digite q quantidade de valores: '))
for i in range(1,n+1):
    numero = int(input('Digite um numero: '))
    if numero  <=0:
        print('Numero Invalido.')
    else:
        fatorial = 1
        for j in range(1,numero + 1):
            fatorial = fatorial * j
        print(f'{numero}! = {fatorial}')
