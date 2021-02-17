
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
auxl = l
auxa = a
while auxa >= 1:
    while auxl >=1:
        if auxa == a or auxa == 1:
            print("#", end = "")
            auxl = auxl - 1
        else:
                if auxl == l or auxl == 1:
                    print("#", end = "")
                    auxl = auxl - 1
                else:
                    print(" ", end = "")
                    auxl = auxl - 1
    print("")
    auxl = l    
    auxa = auxa - 1
