print('============== Exercicio 11 ==============')
horas_trabalhadas = int(input('Digite o Numero de Horas Trabalhadas: '))
if horas_trabalhadas <= 40:
    print('Seu Salario será de R$ {:.2f}.'.format(horas_trabalhadas * 15.00))
else:
    print(f'Seu Salario será de R$ {(horas_trabalhadas - 40) * 21.00 + 600.00:.2f}.')
#    horas_trabalhadas40 = horas_trabalhadas - 40
#    print('Seu Salario será de R$ {:.2f}.'.format(600.00 + horas_trabalhadas40 * 21.00))



