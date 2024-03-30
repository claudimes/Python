intervalo_10a20 = 0
intervalo_fora = 0
c = 1
while c < 11:
    numero = int(input(f'Digite o {c}º numero:'))
    c = c + 1
    if numero >= 10 and numero <= 20:
        intervalo_10a20 = intervalo_10a20 + 1
    else:
        intervalo_fora = intervalo_fora + 1

print(f'Estão DENTRO do intervalo [10,20]: {intervalo_10a20} ')
print(f'Estão FORA do intervalo [10,20]: {intervalo_fora} ')
