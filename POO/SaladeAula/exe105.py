class Pessoa:
    def __init__(self):
        self.nome = ""
        self.cpf = 0

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.matricula = 0

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.titulacao = " "


class Funcionario(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.cargo = " "
        self.salario = 0


aluno = Aluno()
aluno.nome = "Ana"
aluno.cpf = 123
print(aluno.nome)
print(aluno.matricula)
print(aluno.cpf)

print('-=' * 5)
professor = Professor()
professor.nome = "José"
professor.cpf = 456
print(professor.nome)
print(professor.cpf)

print('-=' * 5)
funcionario = Funcionario()
funcionario.nome = "Lucas"
funcionario.cpf = 789
funcionario.cargo = "Diretor"
funcionario.salario = 19900
print(funcionario.nome)
print(funcionario.cpf)
print(funcionario.cargo)
print(f'Salario: {funcionario.salario:.2f}')

