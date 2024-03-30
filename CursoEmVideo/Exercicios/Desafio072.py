''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez','onze', 'doze', 'treze', 'quatroze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
resposta = 'S'
while resposta == 'S':
    while True:
        num = num = int(input('Digite um NÚMERO entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Voce digitou o numero {cont[num]}.')
    while True:
        resposta = str(input('Deseja continuar? [S]/[N] ')).upper().strip()
        if resposta != 'S' and resposta != 'N':
            print('Tente novamente.', end=' ')
        else:
            if resposta == 'N' or resposta == 'S':
                break







