from datetime import date
print ('================= Desafio 32 =================')
ano = int(input('Que ano que analizar? Coloque 0 para analisar o ano ataul. '))
if ano == 0:
    ano = date.today().year # vai Pegar a data de atual, e depois vai pegar somente o ano.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')
