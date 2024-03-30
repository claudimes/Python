print ('================= Desafio 34 =================')
salario = float(input('Informe seu Salario do Funcionario? '))
if salario > 1250:
    print(f'Se salario de R$ {salario :.2f}, terá um reajuste de 10% e passará para R$ {(salario * 10/100) + salario :.2f}.')
else:
    print(f'Se salario de R$ {salario:.2f}, terá um reajuste de 15% e passará para R$ {(salario * 15 / 100) + salario :.2f}.')
