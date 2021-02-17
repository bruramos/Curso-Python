
def n_primos(n):
    ninicial = n
    auxn = n
    resto = 1
    nao_primo = 0
    while n > 2:
        while auxn > 2 and resto != 0:
            auxn = auxn - 1
            resto = n % auxn
            if resto == 0:
                nao_primo = nao_primo + 1
        n = n - 1
        auxn = n
        resto = 1
    return ninicial - nao_primo-1
