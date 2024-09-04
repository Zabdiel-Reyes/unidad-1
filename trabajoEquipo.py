class datos:
    def __init__ (self):
        self.cali1=float(input("ingresa la primera calificacion:"))
        self.cali2=float(input("ingresa la segunda calificacion:"))
        self.cali3=float(input("ingresa la tercera calificacion:"))
        self.nombre=input("ingresa el nombre del alumno:")
        self.promedio=0
    def promedio_(self):
     self.promedio= (self.cali1+self.cali2+self.cali3)/3
     print(f"\npromedio de {self.nombre}: {self.promedio}")
    def comparacion(self):
        if (self.promedio>=70):
           print(f"\n\tel alumno {self.nombre} esta aprobado")
        else:
           print(f"\n\tel alumno {self.nombre} esta aprobado")
         
alumno=datos()
alumno.promedio_()
alumno.comparacion()