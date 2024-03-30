n = int(input('Digite um Numero para ver sua tabuada: '))
print(f'A Tabuada de {n} é:')
for i in range(1, n + 1):
    print(f'{i} x {n} = ', i * n)
