class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h


class Rectangulo(Poligono):
    def area(self):
        return self.b * self.h


class Triangulo(Poligono):
    def area(self):
        return (self.b * self.h) / 2


def mostrarMenu():
    print("Elige una figura cuya área desea calcular: ")
    print("1.- Triángulo")
    print("2.- Rectángulo")
    print("3.- Salir")


def solicitarDatos(figura):
    ba = float(input(f"Escribe la base del {figura}: "))
    ha = float(input(f"Escribe la altura del {figura}: "))
    return ba, ha


while True:
    mostrarMenu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        
        ba, ha = solicitarDatos("triángulo")
        triangulo = Triangulo(ba, ha)
        print("Área del triángulo:", triangulo.area())

    elif opcion == '2':
        
        ba, ha = solicitarDatos("rectángulo")
        rectangulo = Rectangulo(ba, ha)
        print("Área del rectángulo:", rectangulo.area())

    elif opcion == '3':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
