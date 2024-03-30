print('============== Exercicio 13 ==============')
ano_carro = int(input('Qual é o Ano do Carro: '))
peso_modelo = float(input('Qual o Peso do Modelo deste Automovel: '))
if ano_carro <= 1970 and peso_modelo < 1200:
    print('Classe de peso é 1. A taxa de registro para o carro sera $ 16,50. ')
else:
    if ano_carro <= 1970 and peso_modelo > 1200 and peso_modelo <= 1700:
        print('Classe de peso é 2. A taxa de registro para o carro sera $ 25,50. ')
    else:
        if ano_carro <= 1970 and peso_modelo > 1700:
            print('Classe de peso é 3. A taxa de registro para o carro sera $ 46,50. ')
        else:
            if ano_carro >= 1971 and ano_carro <= 1979 and peso_modelo < 1200:
                print('Classe de peso é 4. A taxa de registro para o carro sera $ 27,00. ')
            else:
                if ano_carro >= 1971 and ano_carro <= 1979 and peso_modelo >= 1200 and peso_modelo <= 1700:
                    print('Classe de peso é 5. A taxa de registro para o carro sera $ 30,50. ')
                else:
                    if ano_carro >= 1971 and ano_carro <= 1979 and peso_modelo > 1700:
                        print('Classe de peso é 6. A taxa de registro para o carro sera $ 52,50. ')
                    else:
                        if ano_carro >= 1980 and peso_modelo < 1600:
                            print('Classe de peso é 7. A taxa de registro para o carro sera $ 19,50. ')
                        else:
                            print('Classe de peso é 8. A taxa de registro para o carro sera $ 55,50. ')
