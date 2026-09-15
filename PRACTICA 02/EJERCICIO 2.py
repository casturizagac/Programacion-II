import math
class AlgebraVectorial:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def producto_punto(self, b):
        return self.x * b.x + self.y * b.y
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)
    # a)
    def perpendicular_a(self, b):
        suma = AlgebraVectorial(self.x + b.x, self.y + b.y)
        resta = AlgebraVectorial(self.x - b.x, self.y - b.y)
        return suma.magnitud() == resta.magnitud()
    # b)
    def perpendicular_b(self, b):
        suma = AlgebraVectorial(self.x + b.x, self.y + b.y)
        resta = AlgebraVectorial(b.x - self.x, b.y - self.y)
        return suma.magnitud() == resta.magnitud()
    # c)
    def perpendicular_b(self, b):
        return self.producto_punto(b) == 0
    # d)
    def perpendicular_c(self, b):
        suma_x = self.x + b.x
        suma_y = self.y + b.y
        izquierda = suma_x**2 + suma_y**2
        derecha = self.magnitud()**2 + b.magnitud()**2
        return izquierda == derecha
    # e)
    def paralelo_a(self, b):
        if b.x != 0:
            r = self.x / b.x
            return self.y == r * b.y
        if b.y != 0:
            r = self.y / b.y
            return self.x == r * b.x
        return True
    # f)
    def paralelo_b(self, b):
        cruz = self.x * b.y - self.y * b.x
        return cruz == 0
    # g)
    def proyeccion_de_a_sobre_b(self, b):
        arriba = self.producto_punto(b)
        abajo = b.magnitud()**2
        return arriba / abajo
    # h)
    def componente_de_a_en_b(self, b):
        arriba = self.producto_punto(b)
        return arriba / b.magnitud()

a = AlgebraVectorial(3, 4)
b = AlgebraVectorial(4, -3)

print("Vector a: ", a.x, a.y)
print("Vector b: ", b.x, b.y)

print("Producto punto: ", a.producto_punto(b))

print("¿Son perpendiculares?")
print(a.perpendicular_a(b))
print(a.perpendicular_b(b))
print(a.perpendicular_c(b))

print("¿Son paralelos?")
print(a.paralelo_a(b))
print(a.paralelo_b(b))

print("Proyección de a sobre b: ", a.proyeccion_de_a_sobre_b(b))
print("Componente de a en b: ", a.componente_de_a_en_b(b))