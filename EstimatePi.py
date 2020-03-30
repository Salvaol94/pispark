from random import random as rnd

def estimar_pi(calculos):
    dentro_del_circulo = 0
    for I in range(calculos):
        x = rnd()
        y = rnd()
        distancia_al_centro = x * x + y * y
        if distancia_al_centro <= 1:
            dentro_del_circulo += 1;
    return (dentro_del_circulo / calculos) * 4




