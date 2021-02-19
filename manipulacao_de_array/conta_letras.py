def conta_letras(frase, contar="vogais"):
    
    tamanho_frase = len(frase)
    espacos = frase.count(" ")
    vogais_min = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
    vogais_mai = frase.count("A") + frase.count("E") + frase.count("I") + frase.count("O") + frase.count("U")

    total_vogais = vogais_min + vogais_mai

    if contar == "vogais":
        return total_vogais
    if contar == "consoantes":
        return tamanho_frase - total_vogais - espacos
