from SurpresaPi.Curso import Curso
from SurpresaPi.Escolaridade import Escolaridade
from SurpresaPi.Professor import Professor

print('B) Qual a escolaridade de um Cordenador de um curso?')

escolaridade = Escolaridade('Doutor')

professor = Professor('Luciano')
professor.setEscolaridade(escolaridade)

curso = Curso('Engenharia')
curso.setCordenador(professor)

print(curso.getEscolaridadeCordenador())
