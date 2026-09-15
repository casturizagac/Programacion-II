import math
class MiPunto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, *args):

        if len(args) == 1:
            punto = args[0]
            x2 = punto.x
            y2 = punto.y
        elif len(args) == 2:
            x2 = args[0]
            y2 = args[1]
        distancia = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        return distancia
    
p1 = MiPunto()
p2 = MiPunto(10, 30)

print("Punto 1: ", p1.get_x(), p1.get_y())
print("Punto 2: ", p2.get_x(), p2.get_y())
print("Distancia: ", p1.distancia(p2))