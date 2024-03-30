import random
import time

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

qt_de_linhas_e_colunas = int(input('Insira a Quantidade de Linhas e Colunas do Tabuleiro: '))
for linha in range(qt_de_linhas_e_colunas):
    linha = []
    for coluna in range(qt_de_linhas_e_colunas):
        linha.append('*')
    tabuleiro.append(linha)
qt_de_minas = int(input('Insira a Quantidade de Minas a Serem Usadas no Jogo: '))
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


for d in range(len(tabuleiro)):
    lista.append(d)

while len(posicao_bomba) < qt_de_minas:
    linha_bomba = random.choice(lista)
    coluna_bomba = random.choice(lista)
    if [linha_bomba, coluna_bomba] not in posicao_bomba and len(posicao_bomba) < len(tabuleiro):
        posicao_bomba.append([linha_bomba, coluna_bomba])

posicao_bomba.sort() #apagar
while (parar == 'Não') and (contador < ((len(tabuleiro) ** 2))):
    print(posicao_bomba)#apagar
    mostrar_tabuleiro()
    linha_escolha = int(input('Digite a Linha a Ser Jogada: '))
    coluna_escolha = int(input('Digite a Coluna a Ser Jogada: '))
    while (linha_escolha < 0 or coluna_escolha < 0) or (linha_escolha > qt_de_linhas_e_colunas - 1 or coluna_escolha > qt_de_linhas_e_colunas - 1):
        print('Jogada Invalida! Jogue Novamente.')
        linha_escolha = int(input('Digite a Linha a Ser Jogada: '))
        coluna_escolha = int(input('Digite a Coluna a Ser Jogada: '))

    print(f"1 = Abrir Célula / 2 = Marcar Bomba / 3 = Desmarcar Bomba")
    acao = int(input("Selecione a Ação Desejada: "))
    while acao < 1 or acao > 3:
        print('Ops! Tente novamente!')
        print(f"1 = Abrir Célula / 2 = Marcar Bomba / 3 = Desmarcar Bomba")
        acao = int(input("Selecione a Ação Desejada: "))

    while (acao == 1 and tabuleiro[linha_escolha][coluna_escolha] not in '*') or (acao == 2 and tabuleiro[linha_escolha][coluna_escolha] not in '*') or (acao == 3 and tabuleiro[linha_escolha][coluna_escolha] not in 'B') or (qt_de_minas == minas_marcadas):
        if (acao == 1 and tabuleiro[linha_escolha][coluna_escolha] in 'B'):
            print('Célula Marcada com Mina. Desmarque antes de Abrir!')
        else:
            if (acao == 1 and tabuleiro[linha_escolha][coluna_escolha] not in '*'):
                print('Célula já foi Aberta. Tente Novamente!')
            else:
                if acao == 2 and minas_marcadas >= qt_de_minas:
                    print('NÃO é permitido marcar mais minas que o número máximo indicado no início do jogo.')
                else:
                    if acao == 2:
                        print('Celula já esta Marcada. Tente Novamente!')
                    else:
                        if acao == 3:
                            print('Célula NÃO foi marcada ainda. Tente Novamente!')
        mostrar_tabuleiro()
        linha_escolha = int(input('Digite a Linha a Ser Jogada: '))
        coluna_escolha = int(input('Digite a Coluna a Ser Jogada: '))
        while (linha_escolha < 0 or coluna_escolha < 0) or (linha_escolha > qt_de_linhas_e_colunas - 1 or coluna_escolha > qt_de_linhas_e_colunas - 1):
            print('Jogada Invalida! Jogue Novamente.')
            linha_escolha = int(input('Digite a Linha a Ser Jogada: '))
            coluna_escolha = int(input('Digite a Coluna a Ser Jogada: '))

        print(f"1 = Abrir Célula / 2 = Marcar Bomba / 3 = Desmarcar Bomba")
        acao = int(input("Selecione a Ação Desejada: "))

    if ([linha_escolha, coluna_escolha] in posicao_bomba and acao == 1):
        parar = 'Sim'
        #Mostra a posição das Bombas
        for l in range(len(tabuleiro)):
            for c in range(len(tabuleiro)):
                if [l, c] in posicao_bomba:
                    tabuleiro[l][c] = 'B'
    else:
        if acao == 1:
            if [linha_escolha - 1, coluna_escolha] in posicao_bomba and [linha_escolha + 1, coluna_escolha] in posicao_bomba and [
                linha_escolha, coluna_escolha + 1] in posicao_bomba and [linha_escolha,coluna_escolha - 1] in posicao_bomba:
                tabuleiro[linha_escolha][coluna_escolha] = '4'
            else:
                if [linha_escolha - 1, coluna_escolha] in posicao_bomba and [linha_escolha + 1,
                                                                             coluna_escolha] in posicao_bomba and [
                    linha_escolha, coluna_escolha + 1] in posicao_bomba:
                    tabuleiro[linha_escolha][coluna_escolha] = '3'
                else:
                    if [linha_escolha + 1, coluna_escolha] in posicao_bomba and [linha_escolha,
                                                                                 coluna_escolha + 1] in posicao_bomba and [
                        linha_escolha, coluna_escolha - 1] in posicao_bomba:
                        tabuleiro[linha_escolha][coluna_escolha] = '3'
                    else:  # Problema tambem, Marcar 3, porem era 2
                        if [linha_escolha - 1, coluna_escolha] in posicao_bomba and [linha_escolha + 1,
                                                                                     coluna_escolha] in posicao_bomba and [
                            linha_escolha, coluna_escolha - 1] in posicao_bomba:
                            tabuleiro[linha_escolha][coluna_escolha] = '3'
                        else:
                            if [linha_escolha - 1, coluna_escolha] in posicao_bomba and [linha_escolha,
                                                                                         coluna_escolha + 1] in posicao_bomba and [
                                linha_escolha, coluna_escolha - 1] in posicao_bomba:
                                tabuleiro[linha_escolha][coluna_escolha] = '3'
                            else:
                                if [linha_escolha - 1, coluna_escolha] in posicao_bomba and [linha_escolha + 1,
                                                                                             coluna_escolha] in posicao_bomba:
                                    tabuleiro[linha_escolha][coluna_escolha] = '2'
                                else:
                                    if [linha_escolha, coluna_escolha + 1] and [linha_escolha,
                                                                                coluna_escolha - 1] in posicao_bomba:
                                        tabuleiro[linha_escolha][coluna_escolha] = '2'
                                    else:  # 1-0 problema: Mostra 2 b, sendo que tinha 1
                                        if [linha_escolha - 1, coluna_escolha] and [linha_escolha,
                                                                                    coluna_escolha + 1] in posicao_bomba:
                                            tabuleiro[linha_escolha][coluna_escolha] = '2'
                                        else:
                                            if [linha_escolha - 1, coluna_escolha] and [linha_escolha,
                                                                                        coluna_escolha - 1] in posicao_bomba:
                                                tabuleiro[linha_escolha][coluna_escolha] = '2'
                                            else:
                                                if [linha_escolha + 1, coluna_escolha] and [linha_escolha,
                                                                                            coluna_escolha + 1] in posicao_bomba:
                                                    tabuleiro[linha_escolha][coluna_escolha] = '2'
                                                else:
                                                    if [linha_escolha + 1, coluna_escolha] and [linha_escolha,
                                                                                                coluna_escolha - 1] in posicao_bomba:
                                                        tabuleiro[linha_escolha][coluna_escolha] = '2'
                                                    else:
                                                        if [linha_escolha - 1, coluna_escolha] in posicao_bomba:
                                                            tabuleiro[linha_escolha][coluna_escolha] = '1'
                                                        else:
                                                            if [linha_escolha + 1, coluna_escolha] in posicao_bomba:
                                                                tabuleiro[linha_escolha][coluna_escolha] = '1'
                                                            else:
                                                                if [linha_escolha, coluna_escolha + 1] in posicao_bomba:
                                                                    tabuleiro[linha_escolha][coluna_escolha] = '1'
                                                                else:
                                                                    if [linha_escolha,
                                                                        coluna_escolha - 1] in posicao_bomba:
                                                                        tabuleiro[linha_escolha][coluna_escolha] = '1'
                                                                    else:
                                                                        tabuleiro[linha_escolha][coluna_escolha] = '0'

        if acao == 2:
            tabuleiro[linha_escolha][coluna_escolha] = 'B'
            minas_marcadas += 1

        if acao == 3:
            tabuleiro[linha_escolha][coluna_escolha] = '*'
            contador -= 2
            minas_marcadas -= 1

    contador += 1
    jogadas += 1

mostrar_tabuleiro()
if parar == 'Sim':
    print("O Jogo Acabou!")
else:
    print(f'Voce Ganhou com {jogadas} jogadas! Parabens!!!')