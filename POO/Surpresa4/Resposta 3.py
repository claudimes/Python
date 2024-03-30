from Curso import Curso
from Professor import Professor
from Turma import Turma


professor1 = Professor('Marco')
professor2 = Professor('Antônio')

turma1 = Turma()
turma2 = Turma()

curso = Curso('Computação')
curso.AbrirTurmas(turma1)
curso.AbrirTurmas(turma2)

turma1.setProfessor(professor1)
turma2.setProfessor(professor2)

curso.ProfessorLecionaTurmaCurso()





