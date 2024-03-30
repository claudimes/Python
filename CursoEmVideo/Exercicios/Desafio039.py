print('================= Desafio 39 =================')
from datetime import date

ano_nasc = int(input('Qual é o ano do seu Nascimento? '))
ano_atual = date.today().year # vai Pegar a data de atual, e depois vai pegar somente o ano.
idade = (ano_atual - ano_nasc)
print(f'Quem nasceu em {ano_nasc} tem {idade} anos.')
if idade < 18:
    tempo = (18 - idade)
    print(f'Ainda falta {tempo} anos para o alistamento.')
    ano = ano_atual + tempo
    print(f'Seu alistamento será em {ano} ')
else:
    if idade == 18:
        print('Voce tem que se alistar IMEDIATAMENTE.')
    else:
        tempo = (idade - 18)
        print(f'Voce ja deveria ter se alistado ha {tempo} anos.')
        ano = ano_atual - tempo
        print(f'Seu alistamento foi em {ano}')
