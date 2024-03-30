print('================= Desafio 41 =================')
from datetime import date

ano_nasc = int(input('Qual o ano de seu Nascimento: '))
ano_atual = date.today().year
idade = (ano_atual - ano_nasc)
if idade <= 9:
    print(f" Voce tem {idade} anos. Sua Categoria é Mirim.")
else:
    if idade <= 14:
        print(f'Voce tem {idade} anos. Sua Categoria é Infantil.')
    else:
        if idade <= 19:
            print(f'Voce tem {idade} anos. Sua Categoria é Junior.')
        else:
            if idade <= 20:
                print(f'Voce tem {idade} anos. Sua Categoria é Sênior.')
            else:
                print(f'Voce tem {idade} anos. Sua Categoria é Master.')
