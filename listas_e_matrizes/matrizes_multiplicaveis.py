def sao_multiplicaveis(m1, m2):
    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if colunas_m1 == linhas_m2:
        return True
    else:
        return False
