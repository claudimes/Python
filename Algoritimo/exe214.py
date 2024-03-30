print('============== Exercicio 14 ==============')
nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input('Digite a Segunda Nota: '))
trabalho = float(input('Digite a Nota do Trabalho: '))
faltas = int(input('Digite a Faltas: '))
media = (nota1 + nota2 + trabalho) / 3
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or trabalho < 0 or trabalho > 10:
    print('Notas Invalida. Somente Notas entre 0 e 10')
else:
    if faltas >= 16:
        print('Aluno Reprovado por Faltas.')
    else:
        if media >= 6:
            print('Aluno Aprovado!')
        else:
            print('Fazer Prova Final!')
            nota3 = float(input("Digite a Primeira Nota: "))
            nota4 = float(input('Digite a Segunda Nota: '))
            trabalho1 = float(input('Digite a Nota do Trabalho: '))
            media2 = ((nota3 * 3) + (nota4 * 5) + (trabalho1 * 2)) / 10
            if media2 >= 6:
                print('Aluno Aprovado!')
            else:
                print('Aluno Reprovado!')


