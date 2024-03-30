'''Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu
conceito, conforme a tabela abaixo'''

def analise():
    if (media<0 or media>100):
        conceito = 'MEDIA INVALIDA!'
    else:
        if media <= 49:
            conceito = 'D'
        else:
            if media <= 69:
                conceito = 'C'
            else:
                if media <= 89:
                    conceito = 'B'
                else:
                    if media <= 100:
                        conceito = 'A'
    return conceito


media = float(input('Qual a MEDIA do Aluno: '))
print(f'ALUNO com a Media {media}, recebe o CONCEITO: {analise()}')
