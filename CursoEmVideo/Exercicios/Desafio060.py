''' Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 '''

numero = int(input('Digite um numero para ver seu Fatorial: '))
c = numero
f = 1
print(f"Calculando {numero}!")
while c > 0:
    print(c, end=(' '))
    print(' x ' if c > 1 else ' = ', end=(' '))
    f *= c
    c -= 1
print(f)


