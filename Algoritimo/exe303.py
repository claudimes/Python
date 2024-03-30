valor = int(input('Digite um Numero:'))
if valor <= 0:
    print('Valor Invalido')
else:
    fatorial = 1
    for i in range (1 , valor + 1):
        fatorial = fatorial * i
    print(f'{valor}! = {fatorial}')


        