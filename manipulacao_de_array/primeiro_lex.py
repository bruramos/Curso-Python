def primeiro_lex(lista):
    primeiro_ordem = lista[0]
    testa = True

    for i in range(len(lista)):
        palavra_atual = lista[i].lower()
        palavra_anterior = lista[i-1].lower()

        testa = palavra_atual < palavra_anterior
        if testa:
            primeiro_ordem = lista[i]

    return primeiro_ordem


def testa_primeiro_lex():

    print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
    # deve devolver 'A'

    print(primeiro_lex(['AAAAAA', 'b']))
    # deve devolver 'AAAAAA'
    
