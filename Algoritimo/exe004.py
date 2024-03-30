# 4. Calcular o aumento que sera dado a un funcionario, obtendo do usuario as seguintes
# informações: Salario atual e a porcentagem de aumento. Apresentar o novo valor do salario e o valor do
# aumento
salario = float(input('Digite o Salario Atual: '))
porcentagem = float(input('Digite a Porcentagem do Aumento '))
aumento = salario * (porcentagem / 100)
print(f'O aumento foi de R$ = {aumento :.2f}')
print(f'Novo Salario R$ = {salario + aumento:.2f}')

