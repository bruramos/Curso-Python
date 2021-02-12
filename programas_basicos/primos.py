
n = int(input("Digite um número inteiro: "))
aux = n
resto = 1
primo = False

while aux>2 and primo == False:
    aux = aux - 1
    resto = n % aux
    if resto == 0:
        primo = True

if primo == False and n != 1:
    print("primo")
else:
    print("não primo")

