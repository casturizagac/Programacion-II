import math
class Vector:

    def __init__(self, a1, a2, a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
    # a)
    def __add__(self, b):
        return Vector(
            self.a1+b.a1,
            self.a2+b.a2,
            self.a3+b.a3
        )
    # b)
    def __mul__(self, r):
        return Vector(
            r*self.a1,
            r*self.a2,
            r*self.a3
        )
    # c)
    def longitud(self):
        return math.sqrt(
            self.a1**2+
            self.a2**2+
            self.a3**2
        )
    # d)
    def normal(self):
        longitud = self.longitud()

        return Vector(
            self.a1/longitud,
            self.a2/longitud,
            self.a3/longitud
        )
    # e)
    def __matmul__(self, b):
        return (
            self.a1*b.a1 +
            self.a2*b.a2 +
            self.a3*b.a3
        )
    # f)
    def __xor__(self, b):
        return Vector(
            self.a2 * b.a3 - self.a3 * b.a2,
            self.a3 * b.a1 - self.a1 * b.a3,
            self.a1 * b.a2 - self.a2 * b.a1
        )

    def mostrar(self):
        print("(", self.a1, ",", self.a2, ",", self.a3, ")")

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)

print("Vector a:")
a.mostrar()

print("Vector b:")
b.mostrar()

# a)
print("\nSuma de a + b:")
c=a+b
c.mostrar()
# b)
print("\nMultiplicación de a por 2:")
c=a*2
c.mostrar()
# c)
print("\nLongitud de a:")
print(a.longitud())
# d)
print("\nVector normal de a:")
c = a.normal()
c.mostrar()
# e)
print("\nProducto escalar a · b:")
print(a@b)
# f)
print("\nProducto vectorial a x b:")
c=a^b
c.mostrar()