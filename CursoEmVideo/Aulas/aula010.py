'''nome = str(input('Qual é seu Nome? '))
if nome == 'Claudio':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom Dia, {nome}!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua media foi {m :.2}')
if m >= 6.0:
    print('Sua media foi boa. PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')
