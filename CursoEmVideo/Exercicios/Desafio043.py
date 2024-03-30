print('================= Desafio 43 =================')
peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua Altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc}. Abaixo do Peso.')
else:
    if imc <= 25:
        print(f'Seu IMC é {imc :.1f}. Peso Ideal.')
    else:
        if imc <= 30:
            print(f'Seu IMC é {imc :.1f}. Sobrepeso.')
        else:
            if imc <= 40:
                print(f'Seu IMC é {imc :.1f}. Obesidade.')
            else:
                print(f'Seu IMC é {imc :.1f}. Obesidade Mórbida.')