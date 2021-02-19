def ordena(lista):
    fim = len(lista)

    for i in range(fim - 1):
        pos_do_min = i

        for j in range(i+1, fim):
            if lista[j] < lista[pos_do_min]:
                pos_do_min = j

        lista[i], lista[pos_do_min] = lista[pos_do_min], lista[i]

    return lista
    
