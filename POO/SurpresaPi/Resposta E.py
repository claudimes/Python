from SurpresaPi.Professor import Professor
from SurpresaPi.Cidade import Cidade

print('E) Qual a cidade de nascimento de um professor? ')

cidade = Cidade('Rio de Janeiro')

professor = Professor('Marcos')
professor.setNaturalidade(cidade)

print(professor.getCidadeNascimentoProfessor())
