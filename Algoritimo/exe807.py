#7.	Faça uma função recursiva que calcule o fatorial de um número.

def fatorial(n):
    if n == 1:
        return 1

    return n * fatorial(n - 1)

n = int(input('Nª para ver seu Fatorial: '))
print(f'Fatorial de {n}! é {fatorial(n)}')

