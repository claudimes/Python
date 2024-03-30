import random

def criar_tabuleiro(linhas, colunas):
    tabuleiro = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append({'valor': ' ', 'aberto': False, 'marcado': False})
        tabuleiro.append(linha)
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    print('   ', end='')
    for i in range(colunas):
        print(f' {i} ', end='')
    print()

    print('   ', end='')
    print('--- ' * colunas)

    for i in range(linhas):
        print(f' {i} |', end='')
        for j in range(colunas):
            celula = tabuleiro[i][j]
            if celula['aberto']:
                print(f' {celula["valor"]} ', end='')
            elif celula['marcado']:
                print(' M ', end='')
            else:
                print(' * ', end='')
        print()

def posicionar_minas(tabuleiro, num_minas):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    minas_posicionadas = 0
    while minas_posicionadas < num_minas:
        x = random.randint(0, colunas - 1)
        y = random.randint(0, linhas - 1)

        celula = tabuleiro[y][x]
        if celula['valor'] != 'X':
            celula['valor'] = 'X'
            minas_posicionadas += 1

def posicao_valida(tabuleiro, x, y):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    if x < 0 or x >= colunas or y < 0 or y >= linhas:
        return False
    return True

def contar_minas_adjacentes(tabuleiro, x, y):
    direcoes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    count = 0
    for dx, dy in direcoes:
        nx = x + dx
        ny = y + dy

        if posicao_valida(tabuleiro, nx, ny):
            celula = tabuleiro[ny][nx]
            if celula['valor'] == 'X':
                count += 1

    return count

def revelar_celula(tabuleiro, x, y):
    if not posicao_valida(tabuleiro, x, y):
        return

    celula = tabuleiro[y][x]
    if celula['aberto'] or celula['marcado']:
        return

    celula['aberto'] = True

    if celula['valor'] == ' ':
        direcoes = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dx, dy in direcoes:
            nx = x + dx
            ny = y + dy
            revelar_celula(tabuleiro, nx, ny)

def marcar_celula(tabuleiro, x, y):
    if not posicao_valida(tabuleiro, x, y):
        return

    celula = tabuleiro[y][x]
    if celula['aberto']:
        return

    celula['marcado'] = not celula['marcado']

def jogar_campo_minado():
    linhas = int(input("Digite o número de linhas do tabuleiro: "))
    colunas = int(input("Digite o número de colunas do tabuleiro: "))
    num_minas = int(input("Digite o número de minas: "))

    tabuleiro = criar_tabuleiro(linhas, colunas)
    posicionar_minas(tabuleiro, num_minas)

    while True:
        imprimir_tabuleiro(tabuleiro)

        x = int(input("Digite a coluna: "))
        y = int(input("Digite a linha: "))

        opcao = input("Digite 'A' para abrir, 'M' para marcar, ou 'D' para desmarcar: ").upper()

        if not posicao_valida(tabuleiro, x, y):
            print("Posição inválida! Tente novamente.")
            continue

        if opcao == 'A':
            celula = tabuleiro[y][x]
            if celula['marcado']:
                print("Não é possível abrir uma célula marcada.")
                continue

            if celula['valor'] == 'X':
                print("Você perdeu! Fim de jogo.")
                celula['aberto'] = True
                break

            revelar_celula(tabuleiro, x, y)

            if all(all(c['aberto'] or c['valor'] == 'X' for c in linha) for linha in tabuleiro):
                print("Parabéns! Você ganhou!")
                break

        elif opcao == 'M':
            marcar_celula(tabuleiro, x, y)

        elif opcao == 'D':
            marcar_celula(tabuleiro, x, y)

        else:
            print("Opção inválida! Tente novamente.")
            continue

# Exemplo de uso
jogar_campo_minado()

