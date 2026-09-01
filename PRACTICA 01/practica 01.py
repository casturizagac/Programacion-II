import time
class Cronometro:
    def __init__(self):
        self.__inicia = 0
        self.__finaliza = 0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time()

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 100000
    
cronometro = Cronometro()
cronometro.inicia()
numeros = []
for i in range(100000, 0, -1):
    numeros.append(i)
for i in range(len(numeros)):
    menor = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor]:
            menor = j
    aux= numeros[i]
    numeros[i] = numeros[menor]
    numeros[menor] = aux
cronometro.detener()

print("Tiempo transcurrido:", cronometro.lapsoDeTiempo(), "milisegundos")