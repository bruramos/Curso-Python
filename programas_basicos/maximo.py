def maximo(x, y):
    if x > y:
        return x
    else:
        return y

def test_maximo():
    assert maximo (1,2) == 2
    assert maximo (3,2) == 3
    assert maximo (5,20) == 20
    assert maximo (50,2) == 50
    assert maximo (-1,2) == 2
    assert maximo (50,-12) == 50
    
