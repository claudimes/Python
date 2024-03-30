class Turma:
    def __init__(self):
        self.professor = None
        self.disciplina = None
        self.alunos = []

    def setProfessor(self, professor):
        self.professor = professor

    def getProfessor(self):
        return self.professor

    def setDisciplina(self, disciplina):
        self.disciplina = disciplina


    def getDisciplina(self):
         return self.disciplina

    def getNomeDoProfessorTurma(self):
        if self.professor == None:
            return 'Turma Sem Professor'
        else:
            return self.professor.getNome()


    def MatricularAlunosTurma(self, aluno):
        self.alunos.append(aluno)
        self.disciplina = ''


    def ExcluirAlunoTurma(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f'{aluno.getNome()} foi removido da Turma')
        else:
            print(f'{aluno.getNome()} não consta nesta Turma. ')


    def NomeAlunosTurma(self):
        if self.alunos == []:
            print('Turma sem Alunos')
        else:
            for aluno in self.alunos:
                print(aluno.getNome())


    def VerificarAlunoTurma(self, aluno):
        if aluno in self.alunos:
            print(f'{aluno.getNome()} está na Turma')
        else:
            print(f'{aluno.getNome()} não esta na Turma.')


    def DisciplinaTurma(self):
        return self.disciplina.getDescricao()





