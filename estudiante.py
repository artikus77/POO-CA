import random


class Estudiante:
    """
    Plantilla para crear estudiantes.
    """

    def __init__(self, nombre, apellido, nota):
        self.id = random.randint(1000, 9999)
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido

    def obtener_estado(self):
        if self.nota >= 61:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrar_informacion(self):
        print("ID:", self.id)
        print("Nombre:", self.obtener_nombre_completo())
        print("Nota:", self.nota)
        print("Estado:", self.obtener_estado())
        print("-------------------------")

    def convertir_a_texto(self):
        return (
            str(self.id) + "," +
            self.nombre + "," +
            self.apellido + "," +
            str(self.nota)
        )
        
      