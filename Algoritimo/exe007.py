print('============== Exercicio 07 ==============')
quilowatts = int(input('Informe o Consumo de Quilowatts: '))
valor_hora = 0.12
valor = (quilowatts * valor_hora)
imposto = (valor * 0.18)
print('O Valor a Pagar sera de R$: ',valor + imposto)
