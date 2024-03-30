from Aluno import Aluno
from Curso import Curso


aluno1 = Aluno('Maria')
aluno2 = Aluno('Antônio')

curso = Curso('Engenharia de Software')

curso.RegistroAlunoCurso(aluno1)

curso.VerificarAlunoCurso(aluno1)
curso.VerificarAlunoCurso(aluno2)


