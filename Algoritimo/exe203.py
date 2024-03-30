print('============== Exercicio 03 ==============')
nota = int(input('Digite a Nota: '))
if nota < 0 or nota > 100:
    print('Nota Invalida')
else:
    if nota >= 60:
        print('Aprovado')
    else:
        print('Reprovado')
