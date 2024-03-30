class Curso:
    def __init__(self, nome_curso):
        self.nome_curso = nome_curso
        self.turmas = []
        self.alunos = []

    def setNomeCurso(self, nome_curso):
        self.nome_curso = nome_curso

    def getNomeCurso(self):
        return self.nome_curso

    def ProfessorLecionaTurmaCurso(self):
        for turma in self.turmas:
            print(turma.getNomeDoProfessorTurma())


    def AlunosTurmaCurso(self):
        for turma in self.turmas:
            turma.NomeAlunosTurma()


    def RegistroAlunoCurso(self, aluno):
        self.alunos.append(aluno)

    def ListaRegistroAlunoCurso(self):
        if self.alunos == []:
            print('Curso sem Alunos')
        else:
            for aluno in self.alunos:
                print(aluno.getNome())


    def ExcluirAlunoCurso(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f'{aluno.getNome()} removido!')
        else:
            print(f'{aluno.getNome()} não está na lista de alunos!')


    def VerificarAlunoCurso(self, aluno):
        if aluno in self.alunos:
            print(f'{aluno.getNome()} está matriculado no Cursos de: {self.nome_curso}')
        else:
            print(f'{aluno.getNome()} não está matriculado no Cursos de: {self.nome_curso}')


    def AbrirTurmas(self, turma):
        self.turmas.append(turma)


    def VerificarTurmaCurso(self, turma):
        if turma in self.turmas:
            print(f'Turma está aberta para o Curso de: {self.nome_curso}')
        else:
            print(f'Turma não Registrada para o Curso de {self.nome_curso}')


    def ExcluirTurmaCurso(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)
            print('Turma Removida')
        else:
            print('Turma não esta registra no Curso')


    def DisciplinaTurmaCurso(self):
        if self.turmas == []:
            print('Sem Turma Registrada')
        else:
            for turma in self.turmas:
                print(turma.DisciplinaTurma())

