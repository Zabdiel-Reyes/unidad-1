class Triangulo:
  """Define un Triangulo segun su base y su altura"""
  def __init__(self,b,h):
    self.b=b
    self.h=h
  def area(self):
   r= (self.b * self.h)/2
   return r

ba=float(input(" Escribe la base: "))
ha=float(input(" Escribe la altura: "))
triangulo= Triangulo (ba, ha)

print ("Área del Triángulo cuya base es",ba, " y altura de",ha,"su área es:", triangulo.area())