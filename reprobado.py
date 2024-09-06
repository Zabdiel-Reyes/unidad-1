
'''class Calificaciones:
  def _init_(self):
    self.c1=0
    self.c2=0
    self.c3=0
    self.n=""
  def prom(self):
    r=(self.c1+self.c2+self.c3)/3
    return r
  def comparacion(self,num):
    if num>=70:
      rs= "Aprobado"
    else:
      rs= "Reprobado"
    return rs

cal =Calificaciones()
cal.n=input("Ingresa tu nombre: ")
cal.c1=float(input("Ingresa la primer calificación: "))
cal.c2=float(input("Ingresa la segunda calificación: "))
cal.c3=float(input("Ingresa la tercer calificación: "))
#cal.comparacion(cal.prom())
p=cal.prom()
c=cal.comparacion(p)
print(cal.n," con calificacionesde : " , cal.c1," ",  cal.c2, " ", cal.c3, ". Con promedio de: ", p, ", es: ",c)'''

class Calificaciones:
    def __init__(self):
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.n = ""

    def prom(self):
        r = (self.c1 + self.c2 + self.c3) / 3
        return r

    def reprobo_alguna_unidad(self):
        materia_reprobada = ""
        if self.c1 < 70:
            materia_reprobada = "la primera materia"
        elif self.c2 < 70:
            materia_reprobada = "la segunda materia"
        elif self.c3 < 70:
            materia_reprobada = "la tercera materia"
        return materia_reprobada

    def comparacion(self, num):
        materia_reprobada = self.reprobo_alguna_unidad()
        if materia_reprobada:
            return f"Reprobado por {materia_reprobada}"
        elif num >= 70:
            return "Aprobado"
        else:
            return "Reprobado"

cal = Calificaciones()
cal.n = input("Ingresa tu nombre: ")
cal.c1 = float(input("Ingresa la calificación de la primera materia: "))
cal.c2 = float(input("Ingresa la calificación de la segunda materia: "))
cal.c3 = float(input("Ingresa la calificación de la tercera materia: "))

p = cal.prom()
c = cal.comparacion(p)

print(cal.n, " con calificaciones de : ", cal.c1, " ", cal.c2, " ", cal.c3, ". Con promedio de: ", p, ", es: ", c)