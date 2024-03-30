from SurpresaPi.Curso import Curso
from SurpresaPi.Escola import Escola
from SurpresaPi.Professor import Professor

print('I) Quem é o diretor de um Professor?')

professor = Professor('Marco Antonio')
curso = Curso('BES')
escola = Escola()
professor.setCurso(curso)
curso.setEscola(escola)
escola.setDiretor(professor)

print(professor.getDiretordeProfessor())





