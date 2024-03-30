# Calcular o aumento que será dado a um funcionário, obtendo do usuário as seguintes informações:
# salário atual e a porcentagem de aumento. Apresentar o novo valor do salário e o valor do aumento.

class Funcionario:

    def __init__(self):
        self.salario_atual = 0
        self.porcentagem_aumento = 0

    def aumento(self):
        return (self.salario_atual * self.porcentagem_aumento) / 100

    def novo_salario(self):
        return self.salario_atual + self.aumento()


funcionario1 = Funcionario()
funcionario1.salario_atual = 5000
funcionario1.porcentagem_aumento = 10

print(f'Novo Salário: R$ {funcionario1.novo_salario():.2f}')
print(f'Valor do Aumento: R$ {funcionario1.aumento():.2f}')
