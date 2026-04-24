import math
from figuras import Figura, abstractmethod

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self): return self.lado ** 2
    def perimetro(self): return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self): return math.pi * (self.radio ** 2)
    def perimetro(self): return 2 * math.pi * self.radio