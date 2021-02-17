def encontra_impares(lista, n = 0, impares = []):
 
    if n == len(lista):
        return impares
    elif lista[n] % 2 == 0:
        return encontra_impares(lista, n + 1, impares)
    else:
        impares.append(lista[n])
        return encontra_impares(lista, n + 1, impares)
        
    
