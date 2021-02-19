def remove_repetidos(lista):
    lista_sort = sorted(lista)
    lista_final = []
    for x in range(len(lista_sort)):
        if lista_sort[x] != lista_sort[x-1]:
            lista_final.append(lista_sort[x])
            x = x - 1
    return lista_final
