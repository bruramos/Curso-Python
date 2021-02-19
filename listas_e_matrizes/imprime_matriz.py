def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end="")
            if j < colunas -1:
                print(" ", end="")
        print()
        

def testa_matriz():
    imprime_matriz([[1], [2]])
    imprime_matriz([[1,2], [2,1]])
    imprime_matriz([[1,2,3], [2,1,4]])
    imprime_matriz([[1,2,3,4], [2,1,4,5]])
    imprime_matriz([[1,2,3,4], [2,1,4,5], [2,4,5,6]])
