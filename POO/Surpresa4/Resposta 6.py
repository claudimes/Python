from Curso import Curso
from Disciplina import Disciplina
from Turma import Turma


disciplina1 = Disciplina('Orientação a Objetos')
disciplina2 = Disciplina('Análise de Sistemas')

turma1 = Turma()
turma2 = Turma()
turma1.setDisciplina(disciplina1)
turma2.setDisciplina(disciplina2)

curso = Curso('Engenharia de Software')

curso.AbrirTurmas(turma1)
curso.AbrirTurmas(turma2)

curso.DisciplinaTurmaCurso()









