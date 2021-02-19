def soma_matrizes(m1, m2):
    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])
    soma = []
    igual = True
    if linhas_m1 != linhas_m2 or colunas_m1 != colunas_m2:
        igual = False
        return igual
    else:
        for i in range(linhas_m1):
            linha_soma = []
            for j in range(colunas_m1):
                valor = m1[i][j] + m2[i][j]
                linha_soma.append(valor)

            soma.append(linha_soma)
        return soma

#soma_matrizes([[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]])
