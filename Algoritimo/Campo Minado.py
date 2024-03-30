import random
from time import sleep

tabuleiro = []
posicao_bomba = []
lista = []
linha = 0
coluna = 0
linha_bomba = 0
coluna_bomba = 0
contador = 0
parar = 'Não'
jogadas = 0
minas_marcadas = 0
sair = 'Nao'

print('-=' * 27)
print('\033[7m                 🏴💣 CAMPO MINADO 🏴💣             \033[m')
print('-=' * 27)
sleep(1)
qt_de_linhas_e_colunas = int(input('\033[1mInsira a Quantidade de Linhas e Colunas do Tabuleiro:\033[m '))
while qt_de_linhas_e_colunas <= 1:
    print('\033[1;31mQuantidade Invalida!\033[m')
    qt_de_linhas_e_colunas = int(input('\033[1mInsira a Quantidade de Linhas e Colunas do Tabuleiro:\033[m '))
for linha in range(qt_de_linhas_e_colunas):
    linha = []
    for coluna in range(qt_de_linhas_e_colunas):
        linha.append('*')
    tabuleiro.append(linha)

qt_de_minas = int(input('\033[1mInsira a Quantidade de Minas a Serem Usadas no Jogo:\033[m '))
if qt_de_minas < 1:
  qt_de_minas = 1
else:
  if qt_de_minas > (len(tabuleiro) ** 2) / 2:
    qt_de_minas = (len(tabuleiro) ** 2) // 2

def mostrar_tabuleiro():
    colunas = len(tabuleiro[0])
    print('  ', end='')
    for a in range(colunas):
        print(' ', a, end=' ')
    print()
    for b in range(0, qt_de_linhas_e_colunas):
        print(b, end=' ')
        for c in range(0, qt_de_linhas_e_colunas):
            print(f'| {tabuleiro[b][c]}', end=' ')
        print('|')

def escolher_linha_coluna():
    global linha_escolha
    global coluna_escolha
    global acao
    mostrar_tabuleiro()
    linha_escolha = int(input('\033[1mDigite a Linha a Ser Jogada:\033[m '))
    coluna_escolha = int(input('\033[1mDigite a Coluna a Ser Jogada:\033[m '))

    while (linha_escolha < 0 or coluna_escolha < 0) or (linha_escolha > qt_de_linhas_e_colunas - 1 or coluna_escolha > qt_de_linhas_e_colunas - 1):
        print('\033[1;31mJogada Invalida! Jogue Novamente.\033[m')
        linha_escolha = int(input('\033[1mDigite a Linha a Ser Jogada:\033[m '))
        coluna_escolha = int(input('\033[1mDigite a Coluna a Ser Jogada:\033[m '))

    print(f"\033[1;33m1 = Abrir Célula / 2 = Marcar Mina / 3 = Desmarcar Mina\033[m")
    acao = int(input("\033[1;33mSelecione a Ação Desejada:\033[m "))

    while acao < 1 or acao > 3:
        print('\033[1;31mOps! Tente novamente!\033[m')
        print(f"\033[1;33m1 = Abrir Célula / 2 = Marcar Mina / 3 = Desmarcar Mina\033[m")
        acao = int(input("\033[1;33mSelecione a Ação Desejada:\033[m "))


for d in range(len(tabuleiro)):
    lista.append(d)

while len(posicao_bomba) < qt_de_minas:
    linha_bomba = random.choice(lista)
    coluna_bomba = random.choice(lista)
    if [linha_bomba, coluna_bomba] not in posicao_bomba and len(posicao_bomba) < (len(tabuleiro)**2):
        posicao_bomba.append([linha_bomba, coluna_bomba])

posicao_bomba.sort()
print('-=' * 27)
print(f'\033[1;37mGerando Tabuleiro {len(tabuleiro)} x {len(tabuleiro)} com {qt_de_minas} Minas...\033[m')
sleep(1)
print(f"\033[1;37mLoading....\033[m")
sleep(1)
print('\033[1;37m       Boas-vindas ao Campo Minado!\033[m')
sleep(1)


while (parar == 'Não') and (contador < ((len(tabuleiro) ** 2))):
    print('-=' * 27)
    # print(f'Jogada: {jogadas} - Contador {contador}')
    # print(posicao_bomba)
    escolher_linha_coluna()

    if acao == 1:
        if tabuleiro[linha_escolha][coluna_escolha] in 'B':
                print('\033[1;31mOps! Célula está marcada como mina.\033[m')
                sair = 'Sim'
        else:
            if tabuleiro[linha_escolha][coluna_escolha] not in '*':
                print('\033[1;31mEsta célula já está aberta!\033[m')
                sair = 'Sim'
            else:
                sair = 'Nao'
    if acao == 2:
        if (minas_marcadas == qt_de_minas):
            print('\033[1;31mNÃO é permitido marcar mais minas que o número Máximo indicado no início do jogo.\033[m')
            sair = 'Sim'
        else:
            if tabuleiro[linha_escolha][coluna_escolha] in 'B':
                print('\033[1;31mCelula já esta Marcada!\033[m')
                sair = 'Sim'
            else:
                if tabuleiro[linha_escolha][coluna_escolha] not in '*':
                    print('\033[1;31mCelula já esta Aberta!\033[m')
                    sair = 'Sim'
                else:
                    tabuleiro[linha_escolha][coluna_escolha] = 'B'
                    print("\033[1;34mCélula marcada como mina.\033[m")
                    minas_marcadas += 1
                    sair = 'Nao'
    if acao == 3:
        if tabuleiro[linha_escolha][coluna_escolha] not in 'B':
            print('\033[1;31mCélula NÃO foi marcada ainda!\033[m')
            sair = 'Sim'
        else:
            print("\033[1;34mMarcação de mina removida.\033[m")
            tabuleiro[linha_escolha][coluna_escolha] = '*'
            contador -= 2
            minas_marcadas -= 1
            sair = 'Nao'

    if sair == 'Nao':
        if ([linha_escolha, coluna_escolha] in posicao_bomba and acao == 1):
            parar = 'Sim'
            for l in range(len(tabuleiro)):
                for c in range(len(tabuleiro)):
                    if [l, c] in posicao_bomba:
                        tabuleiro[l][c] = '💣'
        else:
            if acao == 1:
                minas = 0
                if [linha_escolha - 1, coluna_escolha] in posicao_bomba:
                    minas += 1
                if [linha_escolha + 1, coluna_escolha] in posicao_bomba:
                    minas += 1
                if [linha_escolha, coluna_escolha + 1] in posicao_bomba:
                    minas += 1
                if [linha_escolha, coluna_escolha - 1] in posicao_bomba:
                    minas += 1
                tabuleiro[linha_escolha][coluna_escolha] = str(minas)

        contador += 1
        jogadas += 1

print('-=' * 27)
mostrar_tabuleiro()
print('-=' * 27)
if parar == 'Sim':
    print("\033[1;31mGame Over! Você foi explodido.\033[m")
    print(f'Posição das Minas: {posicao_bomba}')
else:
    print(f'\033[1;32mVocê Ganhou com {jogadas} jogadas! Parabens!!!\033[m')
print('-=' * 27)
print('FIM DE JOGO! Até a Próxima!')