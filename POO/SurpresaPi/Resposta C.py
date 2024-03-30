from SurpresaPi.Escola import Escola
from SurpresaPi.Escolaridade import Escolaridade
from SurpresaPi.Professor import Professor

print('C) Qual a escolaridade do Diretor de uma escola?')

escolaridade = Escolaridade('Mestrado')

professor = Professor('Marco')
professor.setEscolaridade(escolaridade)

escola = Escola()
escola.setDiretor(professor)

print(escola.getEscolaridadeDiretor())
