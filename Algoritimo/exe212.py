print('============== Exercicio 12 ==============')
tempo_deposito = float(input("Digite o Tempo em que os Fundos estão Depositados:  "))
if tempo_deposito >= 5:
    print('Seus Fundos estão aplicados a {} anos. Sua Taxa de Juros é R$ 0,95.'.format(tempo_deposito))
else:
    if tempo_deposito >= 4:
        print('Seus Fundos estão aplicados a {} anos. Sua Taxa de Juros é R$ 0,90.'.format(tempo_deposito))
    else:
        if tempo_deposito >= 3:
            print('Seus Fundos estão aplicados a {} anos. Sua Taxa de Juros é R$ 0,85.'.format(tempo_deposito))
        else:
            if tempo_deposito >= 2:
                print('Seus Fundos estão aplicados a {} anos. Sua Taxa de Juros é R$ 0,75.'.format(tempo_deposito))
            else:
                if tempo_deposito >= 1:
                    print('Seus Fundos estão aplicados a {} anos. Sua Taxa de Juros é R$ 0,65.'.format(tempo_deposito))
                else:
                    print('Seus Fundos estão aplicados a {} meses. Sua Taxa de Juros é R$ 0,55.'.format(tempo_deposito))
