print('================= Desafio 40 =================')
n1 = float(input('Qual é a primeira Nota: '))
n2 = float(input('Qual é a Segunda Nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua Media foi {media :.1f}. Repovado!')
else:
    if media < 6.9:
        print(f'Sua Media foi {media :.1f}. Recuperação!')
    else:
        print(f'Sua Media foi {media :.1f}. Aprovado!')

