from Aluno import Aluno
from Curso import Curso
from Turma import Turma


aluno1 = Aluno('Claudio')
aluno2 = Aluno('Antônio')

turma1 = Turma()
turma2 = Turma()
turma1.MatricularAlunosTurma(aluno1)
turma2.MatricularAlunosTurma(aluno2)

curso = Curso('Sistema de Informação')
curso.AbrirTurmas(turma1)
curso.AbrirTurmas(turma2)

curso.AlunosTurmaCurso()

