#main utilizado para teste, colocar main() no final
def main():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    print(t1.semelhantes(t2))
    

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        self.perimetro = self.a + self.b + self.c
        return self.perimetro

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        if self.a != self.b != self.c and self.a != self.c:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        ab = self.a**2 + self.b**2
        bc = self.b**2 + self.c**2
        ac = self.a**2 + self.c**2
        if ab == self.c**2 or bc == self.a**2 or ac == self.b**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        self.t1 = [self.a, self.b, self.c]
        self.t2 = [triangulo.a, triangulo.b, triangulo.c]
        self.sort_t1 = sorted(self.t1)
        self.sort_t2 = sorted(self.t2)

        if self.sort_t2[0] % self.sort_t1[0] == 0 and self.sort_t2[1] % self.sort_t1[1] == 0 and self.sort_t2[2] % self.sort_t1[2] == 0:
            return True
        else:
            return False

