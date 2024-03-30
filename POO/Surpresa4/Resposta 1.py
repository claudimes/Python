from Professor import Professor
from Turma import Turma

turma = Turma()
professor = Professor('Marco Antônio')
turma.setProfessor(professor)
print(turma.getNomeDoProfessorTurma())

