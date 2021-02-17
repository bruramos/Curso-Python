def maximo(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z

def test_maximo():
    assert maximo (1,2,3) == 3
    assert maximo (3,2,1) == 3
    assert maximo (5,20,4) == 20
    assert maximo (50,2,60) == 60
    assert maximo (-1,2,-10) == 2
    assert maximo (50,-12,10) == 50
    
