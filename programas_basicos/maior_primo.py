def primo(n):
    aux = n
    resto = 1
    primo = True

    while aux>2 and primo == True:
        aux = aux - 1
        resto = n % aux
        if resto == 0:
            primo = False

    if primo == True and n != 1:
        primo = True
    else:
        primo = False

    return primo

def maior_primo(n):
    while primo(n) == False:
        n = n - 1
    return n


def test_primo():
    assert primo(1) == False
    assert primo(2) == True
    assert primo(4) == False
    assert primo(13) == True
    assert primo(35) == False
    assert primo(100) == False
    assert primo(101) == True


def test_maior_primo():
    assert maior_primo(100) == 97
    assert maior_primo(7) == 7
    assert maior_primo(78) == 73
