soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}º Nmero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A Soma dos {cont} Numeros PARES é {soma}.')
