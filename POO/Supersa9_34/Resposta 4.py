from Departamento import Departamento
from Escolaridade import Escolaridade
from Funcionario import Funcionario

print('Qual a escolaridade do chefe de um departamento?')

escolaridade = Escolaridade('Pós-Graduação')
chefe = Funcionario('Gomes')
departamento = Departamento()
chefe.setEscolaridade(escolaridade)
departamento.setChefia(chefe)

print(departamento.getEscolaridadeChefeDepartamento())
