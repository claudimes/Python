#Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade.
#A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente
#(12 a 17 anos), adulta (18 a 64 anos) ou idosa (65 anos em diante).

print('============== Exercicio 08 ==============')
ano_nascimento = int(input('Digite seu Ano de Nascimento: '))
ano_atual = int(input('Digite o Ano Atual: '))
idade = ano_atual - ano_nascimento

if idade <= 3:
    print('Sua Idade é: {} anos. Bebê'.format(idade))
else:
    if idade <= 11:
        print('Sua idade é: {} anos. Criança'.format(idade))
    else:
        if idade <= 17:
            print('Sua Idade é: {} anos. Adolecente'.format(idade))
        else:
            if idade <= 64:
                print('Sua Idade é: {} anos. Adulta'.format(idade))
            else:
                print('Sua Idade é: {} anos. Idosa'.format(idade))


