#Ler um número e informar se ele é positivo, negativo ou neutro (zero).

print('============== Exercicio 06 ==============')
numero = int(input('Digite um Numero: '))
if numero == 0:
    print('{} é Neutro.'.format(numero))
else:
    if numero > 0:
        print('{} é Positivo.'.format(numero))
    else:
        print('{} é negativo.'.format(numero))
