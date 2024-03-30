print('============== Exercicio 17 ==============')
codigo = int(input('Digite o Codigo da Unidade de Disco: '))
if codigo == 1:
    print("Codigo: {} - CD-ROM (700MB).".format(codigo))
else:
    if codigo == 2:
        print("Codigo: {} - DVD-ROM (4.7GB).".format(codigo))
    else:
        if codigo == 3:
            print("Codigo: {} - DVD-9 (8.54 GB).".format(codigo))
        else:
            if codigo == 4:
                print("Codigo: {} - Blu-Ray (25 GB).".format(codigo))

