from time import sleep
velha = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]
         ]
jogadas = 1
parada = 'Nao'
vencedor = ' '
quem_joga = 2  # 1= Jogador O - 2= Jogador X
jogar_novamente = 'S'
vit_x = vit_O = empate = 0

def placar():
    print('-=' * 20)
    print('              \033[7mPLACAR\033[m')
    sleep(0.5)
    print(f'\033[1;4;36m JOGADOR X \033[m                 \033[1;4;37m JOGADOR O \033[m')
    sleep(0.5)
    print('              \033[1mEMPATES\033[m')
    sleep(0.5)
    print(f'   \033[1m{vit_x}             {empate}              {vit_O}\033[m')
    sleep(0.5)
    print('-=' * 20)
    sleep(1)

def tela():
    print("\033[1m    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2],'\033[m')
    sleep(0.5)


def verif_vit():
    global velha
    global vencedor
    global parada
    global vit_O
    global vit_x
    if (velha[0][0] == "X") and (velha[0][1] == "X") and (velha[0][2] == "X") or \
            (velha[1][0] == "X") and (velha[1][1] == "X") and (velha[1][2] == "X") or \
            (velha[2][0] == "X") and (velha[2][1] == "X") and (velha[2][2] == "X") or \
            (velha[0][0] == "X") and (velha[1][0] == "X") and (velha[2][0] == "X") or \
            (velha[0][1] == "X") and (velha[1][1] == "X") and (velha[2][1] == "X") or \
            (velha[0][2] == "X") and (velha[1][2] == "X") and (velha[2][2] == "X") or \
            (velha[0][0] == "X") and (velha[1][1] == "X") and (velha[2][2] == "X") or \
            (velha[0][2] == "X") and (velha[1][1] == "X") and (velha[2][0] == "X"):
        vencedor = "X"
        vit_x += 1
        parada = 'Sim'
    else:
        if (velha[0][0] == "O") and (velha[0][1] == "O") and (velha[0][2] == "O") or \
                (velha[1][0] == "O") and (velha[1][1] == "O") and (velha[1][2] == "O") or \
                (velha[2][0] == "O") and (velha[2][1] == "O") and (velha[2][2] == "O") or \
                (velha[0][0] == "O") and (velha[1][0] == "O") and (velha[2][0] == "O") or \
                (velha[0][1] == "O") and (velha[1][1] == "O") and (velha[2][1] == "O") or \
                (velha[0][2] == "O") and (velha[1][2] == "O") and (velha[2][2] == "O") or \
                (velha[0][0] == "O") and (velha[1][1] == "O") and (velha[2][2] == "O") or \
                (velha[0][2] == "O") and (velha[1][1] == "O") and (velha[2][0] == "O"):
            vencedor = "O"
            vit_O += 1
            parada = 'Sim'


def novo_jogo():
    global velha
    global jogadas
    global parada
    global vencedor
    global quem_joga
    velha = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]
             ]
    jogadas = 1
    parada = 'Nao'
    vencedor = ' '
    quem_joga = 2  # 1= Jogador O - 2= Jogador X
    print('-=' * 20)
    print('RECOMEÇANDO....')
    sleep(0.5)
    print(f'           .... BOM JOGO! ')
    sleep(0.5)

print('-=' * 20)
print('          \033[1;4;34mJOGO da VELHA!\033[m')
# print('-=' * 20)
sleep(1)
placar()

while jogar_novamente == 'S':
    while (jogadas <= 9) and (parada == 'Nao') and (quem_joga == 2):
        if quem_joga == 2 and jogadas <= 9:
            print('    \033[1;36mJOGADOR X\033[m')
            tela()
            print()  # Print vazio para soltar um linha
            print(f'\033[1;34m {jogadas}ª Jogada\033[m')
            l = int(input('DIGITE LINHA: '))
            c = int(input('DIGITE COLUNA: '))
            while (l < 0 or l > 2) or (c < 0 or c > 2) or (velha[l][c] in 'XO'):
                print('\033[7;40m Jogada Invalida! TENTE NOVAMENTE.\033[m')
                l = int(input('DIGITE LINHA: '))
                c = int(input('DIGITE COLUNA: '))
            velha[l][c] = "X"
            jogadas += 1
            quem_joga = 1
        verif_vit()

        while (jogadas <= 9) and (parada == 'Nao') and (quem_joga == 1):
            if quem_joga == 1 and jogadas <= 9:
                print('-=' * 20)
                print('    \033[1;37mJOGADOR O\033[m')
                tela()
                print()
                print(f'\033[1;34m {jogadas}ª Jogada\033[m')
                l = int(input('DIGITE LINHA: '))
                c = int(input('DIGITE COLUNA: '))
                while (l < 0 or l > 2) or (c < 0 or c > 2) or (velha[l][c] in 'XO'):
                    print('\033[7;40m Jogada Invalida! TENTE NOVAMENTE\033[m')
                    l = int(input('DIGITE LINHA: '))
                    c = int(input('DIGITE COLUNA: '))
                velha[l][c] = "O"
                jogadas += 1
                quem_joga = 2
                verif_vit()

    if vencedor in 'XO':
        print('-=' * 20)
        tela()
        print(f'\033[1;32m Vencedor da Partida: Jogador {vencedor}, com {jogadas - 1} jogadas.\033[m')
        print('\033[1;41m FIM DE JOGO \033[m')
    else:
        print('-=' * 20)
        empate += 1
        tela()
        print('\033[1;32m EMPATE! As Defesas foram eficientes.\033[m')
        print('\033[1;41m FIM DE JOGO \033[m')

    jogar_novamente = str(input('\033[1;33mDeseja Jogar Novamente? [S/N]: \033[m')).upper().strip()[0]
    while jogar_novamente not in 'SN':
        jogar_novamente = str(input('\033[1;33mDeseja Jogar Novamente? [S/N]: \033[m')).upper().strip()[0]
    if jogar_novamente == 'S':
        novo_jogo()
        placar()
    else:
        placar()
        print('\033[1;41m FIM DE JOGO \033[m')
