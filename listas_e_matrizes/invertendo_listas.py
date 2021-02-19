
lista = []
x = 1
while x != 0:
    x = int(input("Digite um número: "))
    if x != 0:
        lista.append(x)
for a in range((len(lista)-1),-1,-1):
    print(lista[a])
