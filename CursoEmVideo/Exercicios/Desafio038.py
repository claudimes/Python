print('================= Desafio 38 =================')
n1 = int(input('Digite o primeiro Numero:'))
n2 = int(input('Qual é o segundo numero: '))
if n1 > n2:
    print('O Primeiro numero é o Maior.')
else:
    if n2 > n1:
        print('O segundo numero é o Maior.')
    else:
        print('Não existe valor maior. Os dois são iguais.')
        