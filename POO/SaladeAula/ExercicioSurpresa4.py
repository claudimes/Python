class Pessoa:
    def __init__(self):
        self.nome = " "
        self.curso = None
        self.turma = None
        self.disciplina = None

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_curso(self, curso):
        self.curso = curso

    def get_curso(self):
        return self.curso

    def set_turma(self, turma):
        self.turma = turma

    def get_turma(self):
        return self.turma

    def set_disciplina(self, disciplina):
        self.disciplina = disciplina

    def get_disciplina(self):
        return self.disciplina


class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

    def nome_do_curso(self):
        if self.curso == None:
            return 'Aluno sem Curso'
        else:
            return self.curso.get_nome()

    def nome_da_turma(self):
        if self.turma == None:
            return 'Aluno sem Turma'
        else:
            return self.turma.get_nome()

    def nome_da_disciplina(self):
        if self.disciplina == None:
            return 'Aluno sem Disciplina.'
        else:
            return self.disciplina.get_nome_disciplina()


class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

    def nome_do_curso(self):
        if self.curso == None:
            return 'Professor sem Curso'
        else:
            return self.curso.get_nome()

    def nome_da_turma(self):
        if self.turma == None:
            return 'Professor sem Turma'
        else:
            return self.turma.get_nome()

    def nome_da_disciplina(self):
        if self.disciplina == None:
            return 'Professor sem Disciplina.'
        else:
            return self.disciplina.get_nome_disciplina()


class Curso:
    def __init__(self):
        self.nome = " "

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

class Turma:
    def __init__(self):
        self.nome = " "

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

class Disciplina:
    def __init__(self):
        self.nome_disciplina = " "

    def set_nome_disciplina(self, nome_disciplina):
        self.nome_disciplina = nome_disciplina

    def get_nome_disciplina(self):
        return self.nome_disciplina

curso = Curso()
curso.set_nome('Engenharia de Software')

disciplina = Disciplina()
disciplina.set_nome_disciplina('Orientação a Objetos')

turma = Turma()
turma.set_nome('A')

aluno = Aluno()
aluno.set_nome("Cláudio Antônio Gomes")
aluno.set_curso(curso)
aluno.set_turma(turma)
aluno.set_disciplina(disciplina)

professor = Professor()
professor.set_nome('Marco Antônio')
professor.set_curso(curso)
professor.set_disciplina(disciplina)
professor.set_turma(turma)

professor2 = Professor()
professor2.set_turma(turma)


print(f'Aluno: {aluno.get_nome()}')
print(f'Curso do Aluno: {aluno.nome_do_curso()}. Disciplina: {aluno.nome_da_disciplina()}. Turma: {aluno.nome_da_turma()}')
print(' ')
print((f"Professor: {professor.get_nome()}"))
print(f'Curso do Professor: {professor.nome_do_curso()}. Disciplina: {professor.nome_da_disciplina()}. Turma: {professor.nome_da_turma()}')


