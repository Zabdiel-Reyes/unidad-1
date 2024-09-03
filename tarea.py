class poligono:
    def __init__(self, b, h):
        self.b = b
        self.h = h
class rectangulo(poligono):
    def area(self):
        return self.b * self.h
class triangulo(poligono):
    def area(self):
        return (self.b * self.h) / 2
def main():
    print("Selecciona una opción:")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    opcion = int(input("Ingresa tu opción: "))
    if opcion == 1:
        ba = float(input("Escribe la base del rectángulo: "))
        ha = float(input("Escribe la altura del rectángulo: "))
        Rectangulo = rectangulo(ba, ha)
        print("Área del rectángulo:", Rectangulo.area())
    elif opcion == 2:
        ba = float(input("Escribe la base del triángulo: "))
        ha = float(input("Escribe la altura del triángulo: "))
        Triangulo = triangulo(ba, ha)
        print("Área del triángulo:", Triangulo.area())
main()
