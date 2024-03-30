'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'cursos', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras: #Analisa cada elemento da Tupla
    print(f'\n Na palavra {p.upper()} temos', end=' ')
    for letra in p:#Analisa cada letra
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
