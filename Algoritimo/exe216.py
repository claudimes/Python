print('============== Exercicio 16 ==============')
cargo = int(input('Digite o Codigo do vendedor: '))
if cargo == 101:
    print("Codigo: {} Cargo: Vendedor.".format(cargo))
else:
    if cargo == 102:
        print("Codigo: {} Cargo: Atendente.".format(cargo))
    else:
        if cargo == 103:
            print("Codigo: {} Cargo: Auxiliar Tecnico.".format(cargo))
        else:
            if cargo == 104:
                print("Codigo: {} Cargo: Assistente.".format(cargo))
            else:
                if cargo == 105:
                    print("Codigo: {} Cargo: Coordenador de Grupo.".format(cargo))
                else:
                    if cargo == 106:
                        print("Codigo: {} Cargo: Gerente.".format(cargo))
                    else:
                        print('Codigo Invalido!')