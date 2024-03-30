from Aluno import Aluno
from Curso import Curso


aluno1 = Aluno('Claudio')
aluno2 = Aluno('Caio')
aluno3 = Aluno('Lara')

curso = Curso('Ciencia da Computação')

curso.RegistroAlunoCurso(aluno1)
curso.RegistroAlunoCurso(aluno2)
curso.RegistroAlunoCurso(aluno3)

curso.ListaRegistroAlunoCurso()
