import os
import random

jogarnovamente = "s"
jogadas = 0
quemjoga = 2 # 1=CPU -  2=Jogador
maxjogadas = 9
vit = "n"
velha = [
    [" ", " ", " "], # L0C0, L0C1, L0C2
    [" ", " ", " "], # L1C0, L1C1, L1C2
    [" ", " ", " "]  # L2C0, L2C1, L2C2
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("   0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))

def jogadorjoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga == 2 and jogadas < maxjogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            velha[l][c]= "X"
            quemjoga = 1
            jogadas += 1
        except:
            print("Jogada Invalida!.")
            os.system("pause")
def cpujoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga == 1 and jogadas < maxjogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quemjoga = 2

def verificarvitoria():
    global velha
    vitoria = "n"
    simbolos =  ["X","O"]
    for s in simbolos:
        vitoria = "n"
        #Verificar linhas
        il = ic= 0
        while (il < 3):
            soma = 0
            ic = 0
            while (ic < 3):
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if(soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break
        #Verificar colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break
        #verifica Diagonal 1
        soma = 0
        indiag = 0
        while indiag < 3:
            if (velha[indiag][indiag] == s):
                soma += 1
            indiag += 1
        if(soma == 3):
            vitoria = s
            break
        #verifica Diagonal 2
        indiagl = 0
        indiagc = 2
        while (indiagc >= 0):
            if (velha[indiagl][indiagc] == s):
                soma += 1
            indiagl += 1
            indiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemjoga
    global maxjogadas
    global vit
    jogadas = 0
    quemjoga = 2  # 1=CPU -  2=Jogador
    maxjogadas = 9
    vit = "n"
    velha = [
        [" ", " ", " "],  # L0C0, L0C1, L0C2
        [" ", " ", " "],  # L1C0, L1C1, L1C2
        [" ", " ", " "]  # L2C0, L2C1, L2C2
    ]

while jogarnovamente == "s":
    while True:
        tela()
        jogadorjoga()
        cpujoga()
        tela()
        vit = verificarvitoria()
        if (vit != "n") or (jogadas >= maxjogadas):
            break

    print('FM DE JOGO.')
    if (vit== "X" or vit == "O"):
        print("Resultado: Jogador: ", vit ,"venceu")
    else:
        print("Resultado: Empate")
    jogarnovamente = input("Jogar Novamente? [s/n] ")
    redefinir()





