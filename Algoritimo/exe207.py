print('============== Exercicio 07 ==============')
salario = float(input('Digite se Salario: '))
tempo_servico = int(input('Informe Quantos Anos de Trabalhados: '))
if tempo_servico <= 1:
    print('O Novo Salario Reajustado é R$ {:.2f}'.format(salario * 1.10))
else:
    print('O Novo Salario Reajustado é de R$ {:.2f}'.format(salario * 1.2))

