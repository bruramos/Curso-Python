def maiusculas(frase):
    tamanho = len(frase)
    maiusculas = ''

    for i in range(tamanho):
        cod = ord(frase[i])
        if cod >= 65 and cod <= 90:
            maiusculas += frase[i]

    return maiusculas
        
