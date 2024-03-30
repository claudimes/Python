from SurpresaPi.Aluno import Aluno
from SurpresaPi.Curso import Curso
from SurpresaPi.Professor import Professor

print('H) Quem é o Cordenador de um Curso de um Aluno?')

professor = Professor('Marco Antônio')

curso = Curso('Computação')
curso.setCordenador(professor)

aluno = Aluno('Miguel')
aluno.setCurso(curso)

print(aluno.getCordenadorCursoAluno())

