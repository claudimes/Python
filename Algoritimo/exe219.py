print('============== Exercicio 19 ==============')
nota = float(input('Digite a Nota do Aluno: '))
if nota >= 9 and nota <= 10:
    print('Nota {} é Conceito A.'.format(nota))
else:
    if nota >= 7 and nota <= 8:
        print('Nota {} é Conceito B.'.format(nota))
    else:
        if nota >= 5 and nota <= 6:
            print('Nota {} é Conceito C.'.format(nota))
        else:
            print('Nota {} é Conceito D.'.format(nota))
    