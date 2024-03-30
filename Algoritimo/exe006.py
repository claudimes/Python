print('============== Exercicio 06 ==============')
salario_b = float(input('Informe o Salario Bruto: '))
hora_extra_trabalhada = int(input('Informe a Quantidade de Horas Extras:'))
valor_hora_extra = float(input('Informe o Valor da Hora Extra: '))
salario_liquido = (salario_b + hora_extra_trabalhada * valor_hora_extra) * 0.88
print('Salario Liquido R$: ',salario_liquido)

