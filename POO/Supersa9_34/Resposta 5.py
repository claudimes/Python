from Empresa import Empresa
from Filial import Filial
from Funcionario import Funcionario

print('Qual o nome do diretor da empresa de uma filial?')
funcionario = Funcionario('Loreval')
diretor = Empresa('Reserva')
filial = Filial()

diretor.setDiretor(funcionario)
filial.setEmpresa(diretor)

print(filial.getNomeDiretorEmpresaFilial())

