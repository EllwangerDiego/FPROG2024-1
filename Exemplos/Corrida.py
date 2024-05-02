import random
import time
import os

def movimentarHamster(posHamster):
        
    p1 = 0
    p2 = 0

    vencedor = 0

    while vencedor == 0:
        time.sleep(0.1)
        os.system ('cls' if os.name == 'nt' else 'clear')

        nroSorteado = random.randint (1,5)
        if nroSorteado == 1:
            p1 = p1 + 1
        elif nroSorteado == 2:
            p1 = p1 + 2
        elif nroSorteado == 3:
            pass
        elif nroSorteado == 4:
            p1 = p1 -1
        else:
            p1 = p1 - 2
        if p1 < 0:
            p1 = 0
        if p1 > 12:
            p1 = 12

            #-------------------------------------------------------------------------------------------------#
        
            nroSorteado = random.randint (1,5)
        if nroSorteado == 1:
            p2 = p2 + 1
        elif nroSorteado == 2:
            p2 = p2 + 2
        elif nroSorteado == 3:
            pass
        elif nroSorteado == 4:
            p2 = p2 -1
        else:
            p2 = p2 - 2
        if p2 < 0:
            p2 = 0
        if p2 > 12:
            p2 = 12

        if p1 == 12:
            vencedor = 1
        if p2 == 12:
            if vencedor == 0:
                vencedor = 2
            else:
                vencedor = 3

        print('Hamster 1: ')
        for n in range(p1):
            print('*', end = '')
        print()

        print('Hamster 2: ')
        for n in range(p2):
            print('*', end = '')
        print()

    if vencedor == 1:
        print('Hamster 1 venceu')
        print()
    elif vencedor == 2:
        print('Hamster 2 venceu')
        print()
    else:
        print('A corrida empatou')
        print()

movimentarHamster(posHamster=0)
        
    