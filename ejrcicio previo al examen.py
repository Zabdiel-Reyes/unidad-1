"""DESAROLLA UN SISTEMA CAJA DE CAMBIO EN EL CUAL SE INSERTA UN BILLETE O SE LE INDICA UNA CANTIDAD A CAMBIAR, EL SISTEMA DEVUELVE LA CANTIDAD EN MODENAS DE 10,5 Y 1 PESO  """
"""REGLA GENERAL NO SE PUEDE DEVOLVER TD DE UNA SOLA MONEDA  TIENE QUE REGRESAR AL MENOS UNA MONEDA DE CADA DENOMINACION."""
"""EJEMPLO LE DAMOS 100"""
class Moneda:
    
    def __init__(self):
        self.lana = 0
        self.uno = 0
        self.cinco = 0
        self.diez = 0

    def pedir_dato(self):
        cantidad = int(input("Ingresa la cantidad de dinero que desea cambiar: "))
        self.lana = cantidad

    def convertir(self):
        while self.lana > 0:
            if self.lana > 10:
                self.lana -= 10
                self.diez += 1
            elif self.lana > 5:
                self.lana -= 5
                self.cinco += 1
            else:
                self.lana -= 1
                self.uno += 1

    def imprime(self):
        print(f"\nSe entregan:\n\t{self.diez} monedas de 10 pesos\n\t{self.cinco} monedas de 5 pesos\n\t{self.uno} monedas de 1 peso")


cambio = Moneda()
cambio.pedir_dato()
cambio.convertir()
cambio.imprime()