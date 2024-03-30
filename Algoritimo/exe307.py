codigo = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
print('='* 10,'Eleições 2023','=' * 10)
print('''
( 1 ) Para Candidato 1
( 2 ) Para Candidato 2  
( 3 ) Para Candidato 3
( 4 ) Para Candidato 4
( 5 ) Voto nulo
( 6 ) Voto em branco
''')
while codigo != 0:
    codigo = int(input('Digite o Codigo do Candidato: '))
    if codigo < 0 or codigo > 7:
        print('Codigo Invalido!')
    if codigo != 0:
        if codigo == 1:
            candidato1 = candidato1 + 1
        else:
            if codigo == 2:
                candidato2 = candidato2 + 1
            else:
                if codigo == 3:
                    candidato3 = candidato3 + 1
                else:
                    if codigo == 4:
                        candidato4 = candidato4 + 1
                    else:
                        if codigo == 5:
                            nulo = nulo + 1
                        else:
                            if codigo == 6:
                                branco = branco + 1

print(f"Total de votos para Candidato 1: {candidato1} votos.")
print(f"Total de votos para Candidato 2: {candidato2} votos.")
print(f"Total de votos para Candidato 3: {candidato3} votos.")
print(f"Total de votos para Candidato 1: {candidato4} votos.")
print(f"Total de votos nulos: {nulo} votos.")
print(f"Total de votos brancos: {branco} votos.")

