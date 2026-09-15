import math
# PROGRAMACION ESTRUCTURADA
def promedio(numeros):
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma / len(numeros)

def desviacion(numeros):
    prom = promedio(numeros)
    suma = 0
    for numero in numeros:
        suma = suma + (numero - prom) ** 2
    return math.sqrt(suma / (len(numeros) - 1))
# PROGRAMACION ORIENTADA A OBJETOS
class Estadistica:
    def __init__(self, numeros):
        self.__numeros = numeros

    def promedio(self):
        suma = 0
        for numero in self.__numeros:
            suma = suma + numero
        return suma / len(self.__numeros)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for numero in self.__numeros:
            suma = suma + (numero - prom) ** 2
        return math.sqrt(suma / (len(self.__numeros) - 1))

# PROGRAMA PRINCIPAL
numeros = list(map(float, input("Ingrese 10 números: ").split()))

print("\nPROGRAMACION ESTRUCTURADA: ")
print("El promedio es: ", promedio(numeros))
print("La desviación estándar es: ", desviacion(numeros))

estadistica = Estadistica(numeros)

print("\nPROGRAMACION ORIENTADA A OBJETOS: ")
print("El promedio es: ", estadistica.promedio())
print("La desviación estándar es: ", estadistica.desviacion())