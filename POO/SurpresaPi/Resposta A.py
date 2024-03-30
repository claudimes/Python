from SurpresaPi.Escolaridade import Escolaridade
from SurpresaPi.Professor import Professor

print('A) Qual a Escolaridade de um Professor?')

escolaridade = Escolaridade("Mestrado")

professor = Professor('Marco')
professor.setEscolaridade(escolaridade)

print(professor.getEscolaridadeProfessor())
