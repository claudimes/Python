from SurpresaPi.Curso import Curso
from SurpresaPi.Professor import Professor

print('J) Quem é o Cordenardor de um Professor?')

curso = Curso('Java')
professor = Professor('Antônio')

curso.setCordenador(professor)
professor.setCurso(curso)

print(professor.getCordenadorProfessor())
