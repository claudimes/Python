negativo = 0
for i in range(1,11):
    n = int(input(f'Digite o {i}º numero: '))
    if n < 0:
        negativo = negativo + 1
print(f'Total de números NEGATIVOS: {negativo}.')
