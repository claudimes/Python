#Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um
#financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o
#salário da pessoa, o algoritmo deverá escrever "Financiamento Concedido"; senão,
#ele deverá escrever "Financiamento Negado".

print('============== Exercicio 10 ==============')
salario = float(input('Informe seu Salario R$: '))
financiamento = float(input('Digite o Valor do Financiamento R$: '))
if financiamento <= salario * 5:
    print('Financiamento Concedido.')
else:
    print('Financiamento Negado!')
    