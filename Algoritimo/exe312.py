numero = 0
contador_seg_0_25= 0
contador_seg_26_50= 0
contador_seg_51_75= 0
contador_seg_76_100= 0

while numero >= 0:
    numero = int(input('Digite um numero de 0 a 100: '))
    if numero < 0:
        print(' ')
    else:
        if numero > 100:
            print('Numero Invalido')
        else:
            if numero >= 0 and numero <=25:
                contador_seg_0_25 = contador_seg_0_25 + 1
            else:
                if numero <= 50:
                    contador_seg_26_50 = contador_seg_26_50 + 1
                else:
                    if numero <= 75:
                        contador_seg_51_75 = contador_seg_51_75 + 1
                    else:
                        if numero <= 100:
                            contador_seg_76_100 = contador_seg_76_100 + 1
print(f' Intervalos de [0,25]: {contador_seg_0_25}.')
print(f' Intervalos de [26,50]: {contador_seg_26_50}.')
print(f' Intervalos de [51,75]: {contador_seg_51_75}.')
print(f' Intervalos de [76,100]: {contador_seg_76_100}.')