print('============== Exercicio 15 ==============')
n1 = int(input("Digite o Primeiro Numero: "))
n2 = int(input("Digite o Segundo Numero: "))
n3 = int(input("Digite o Terceiro Numero: "))
n4 = int(input("Digite o Quarto Numero: "))
if n1 < n2 and n1 < n3 and n1 < n4:
    print("Entre os numeros informados {}, {}, {} e {}, o menor é {}.".format (n1,n2,n3,n4,n1))
else:
    if n2 < n1 and n2 < n3 and n2 < n4:
        print("Entre os numeros informados {}, {}, {} e {}, o menor é {}.".format (n1,n2,n3,n4,n2))
    else:
        if n3 < n2 and n3 < n1 and n3 < n4:
            print("Entre os numeros informados {}, {}, {} e {}, o menor é {}.".format (n1,n2,n3,n4,n3))
        else:
            if n4 < n2 and n4 < n3 and n4 < n1:
                print("Entre os numeros informados {}, {}, {} e {}, o menor é {}.".format (n1,n2,n3,n4,n4))
