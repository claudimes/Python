print('================= Desafio 36 =================')
casa = float(input('Qual é o valor da Casa? R$ '))
salario = float(input('Qual é o valor do seu Salario? R$ '))
anos = int(input('Quantos anos pretende pagar?'))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print(f'Para pagar uma casa de R$ {casa :.2f} em {anos} anos', end='')
print(f'a prestação sera de R$ {prestacao :.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO.')
else:
    print('Emprestimo NEGADO.')
