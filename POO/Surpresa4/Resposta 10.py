from Aluno import Aluno
from Turma import Turma


aluno1 = Aluno('Sergio')
aluno2 = Aluno('Douglas')

turma = Turma()
turma.MatricularAlunosTurma(aluno2)
turma.MatricularAlunosTurma(aluno1)

print('Lista de Aunos Matriculados:')
turma.NomeAlunosTurma()

turma.ExcluirAlunoTurma(aluno2)

print('Lista atualizada de Aunos Matriculados:')
turma.NomeAlunosTurma()


