from Departamento import Departamento
from Empresa import Empresa
from Funcionario import Funcionario
from Grupo import Grupo
from Pais import Pais

print('Qual é o país de alocação de um funcionário?')

pais = Pais('Brasil')
sede = Grupo()
empresa = Empresa('Reserva')
departamento = Departamento()
funcionario = Funcionario('Claudio')

sede.setSede(pais)
empresa.setGrupo(sede)
departamento.setEmpresa(empresa)
funcionario.setAlocacao(departamento)

print(funcionario.getPaisAlocacaoFuncionario())




