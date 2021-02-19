import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    f = 0
    soma = 0
    sab = 0
    while f <= 5:
        soma = soma + abs(as_a[f] - as_b[f])
        f += 1
    sab = soma / 6
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    total_carac_sentenca = 0
    for sentenca in lista_sentencas:
        frases = separa_frases(sentenca)
        lista_frases = lista_frases + frases
        total_carac_sentenca = total_carac_sentenca + len(sentenca)

    lista_palavras = []
    total_carac_frase = 0
    for frase in lista_frases:
        palavras = separa_palavras(frase)
        lista_palavras = lista_palavras + palavras
        total_carac_frase = total_carac_frase + len(frase)
    
    soma_tamanho_palavras = 0
    total_palavras = 0
    for palavra in lista_palavras:
        total_palavras += 1
        soma_tamanho_palavras += len(palavra)
    
    wal = soma_tamanho_palavras / total_palavras
    ttr = n_palavras_diferentes(lista_palavras) / total_palavras
    hlr = n_palavras_unicas(lista_palavras) / total_palavras
    sal = total_carac_sentenca / len(lista_sentencas)
    sac = len(lista_frases) / len(lista_sentencas)
    pal = total_carac_frase / len(lista_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    num_texto = 0
    texto_infectado = 0
    sab = []
    max_sab = 0
    for texto in textos:
        ass_a = calcula_assinatura(texto)
        sab_ab = compara_assinatura(ass_a, ass_cp)
        sab.append(sab_ab)
    max_sab = max(sab)
    texto_infectado = sab.index(max_sab)

    return texto_infectado


def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, ass_cp)
    print("O autor do texto", texto_infectado, "está infectado com COH-PIAH")

main()
