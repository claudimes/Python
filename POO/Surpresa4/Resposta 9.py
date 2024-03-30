from Curso import Curso
from Turma import Turma

turma1 = Turma()
turma2 = Turma()

curso = Curso('Computação')
curso.AbrirTurmas(turma1)

print('Turma 1')
curso.VerificarTurmaCurso(turma1)
print('Turma 2')
curso.VerificarTurmaCurso(turma2)





