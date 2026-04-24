from formas import Cuadrado, Circulo

def ejecutar():
    mi_cuadrado = Cuadrado(5)
    mi_circulo = Circulo(3)
    
    print(f"Área cuadrado: {mi_cuadrado.area()}")
    print(f"Área círculo: {mi_circulo.area():.2f}")

if __name__ == "__main__":
    ejecutar()