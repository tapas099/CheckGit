class Polynomial:
    def __init__(self, *coeff):
        self.coeff = coeff

    def __repr__(self):
        return 'Polynomial(*{})'.format(self.coeff)

    def __add__(self, other):
        return Polynomial(x + y for x, y in zip(self.coeff, other.coeff))


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 5, 3)
p3 = Polynomial('th', 'l', 2)
print(p1+p2)
