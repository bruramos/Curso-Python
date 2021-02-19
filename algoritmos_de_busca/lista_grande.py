import random

def lista_grande(n):
    lista = []

    for i in range(n):
        x = random.randint(0,100)
        lista.append(x)

    return lista
