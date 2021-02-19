def menor_nome(nomes):
    quantidade_nomes = len(nomes)
    menor_nome = nomes[0]

    for i in range(quantidade_nomes):
        tamanho_nome = len(nomes[i].strip())
        tamanho_nome_ant = len(nomes[i-1].strip())

        if tamanho_nome < tamanho_nome_ant:
            menor_nome = nomes[i].strip()

    return(menor_nome.capitalize())

def testa_nome():
    print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
    print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
    print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
    print(menor_nome(['zé', ' lu', 'fê']))
