'''Escrever uma função verificarEstacao(dia, mes), que retorna qual a estação do ano da
data passada por parâmetro. Lembrando que a primavera começa no dia 23 de setembro,
o verão em 21 de dezembro, o outono em 21 de março e o inverno em 21 de junho'''
# Primavera = 23/09 ate 20/12
# Verão = 21/12 ate 20/03
# Outono = 21/03 ate 20/06
# Inverno = 21/06 ate 22/09
def verificarEstacao(dia, mes):
    if (0 < mes > 13) and (0 < dia > 31):
        estacao = 'Estação Invalida! Mes/dia Invalido.'
    else:
        if (dia >= 23 and mes == 9) or (mes == 10) or (mes == 11) or (dia <= 20 and mes == 12):
            estacao = 'PRIMAVERA'
        else:
            if (dia >= 21 and mes == 12) or (mes == 1) or (mes == 2) or (dia <= 20 and mes == 3):
                estacao = 'VERÃO'
            else:
                if (dia >= 21 and mes == 3) or (mes == 4) or (mes == 5) or (dia <= 20 and mes == 6):
                    estacao = 'OUTONO'
                else:
                    if (dia >= 21 and mes == 6) or (mes == 7) or (mes == 8) or (dia <= 22 and mes == 9):
                        estacao = 'INVERNO'
    return estacao


dia = int(input('Qual é o DIA: '))
mes = int(input('Qual é o MÊS:'))
print(f'Nessa data: {dia}/{mes} a ESTAÇÃO do Ano é:', verificarEstacao(dia,mes))

# Primavera = 23/09 ate 20/12
# Verão = 21/12 ate 20/03
# Outono = 21/03 ate 20/06
# Inverno = 21/06 ate 22/09