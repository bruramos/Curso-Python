
   
def partida():

    n = 0
    m = 0
    while m>=n:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    if n%(m+1) == 0:
        print()
        print("Você começa!")
        print()
        usuario = True

    else:
        print("Computador começa!")
        print()
        usuario = False
            
    while n != 0 and usuario:
        pecas_us = usuario_escolhe_jogada(n,m)
        n = n - pecas_us
        print("Agora resta(m) apenas", n, "peça(s) no tabuleiro.")
        print()
        pecas_comp = computador_escolhe_jogada(n,m)
        n = n - pecas_comp
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            print()
        else:
            print("Agora resta(m) apenas", n, "peça(s) no tabuleiro.")
            print()


    while n != 0 and usuario == False:
        pecas_comp = computador_escolhe_jogada(n,m)
        n = n - pecas_comp
        if n == 0:
            print("Fim do jogo! O computador ganhou!")
            print()
        else:
            print("Agora resta(m) apenas", n, "peça(s) no tabuleiro.")
            print()
            pecas_us = usuario_escolhe_jogada(n,m)
            n = n - pecas_us
            print("Agora resta(m) apenas", n, "peça(s) no tabuleiro.")
            print()
            
       
def campeonato():
    total = 1
    while total <= 3:
        print("**** Rodada", total,"****")
        print()
        partida()
        total = total +1
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X", total-1,"Computador")
  
def computador_escolhe_jogada(n,m):
    pecas = m
    meta = m+1
    while (n-m) % meta != 0:
        m = m - 1
    if m == 0:
        print("O computador tirou", pecas, "peça(s).")
        print()
        return pecas
    else:
        print("O computador tirou", m, "peça(s).")
        return m

def usuario_escolhe_jogada(n,m):
    pecas = int(input("Quantas peças você vai tirar? "))
    while pecas > m or pecas <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        pecas = int(input("Quantas peças você vai tirar? "))
    print("Você tirou", pecas, "peça(s).")
    print()
    return pecas

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
p_ou_c = int(input("2 - para jogar um campeonato "))

if p_ou_c == 1:
    print()
    partida()
else:
    print()
    print("Você escolheu um campeonato!")
    print()
    campeonato()

