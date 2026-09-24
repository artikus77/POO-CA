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
from estudiante import Estudiante


# Crear objetos o instancias
estudiante1 = Estudiante("Ana", "López", 85)
estudiante2 = Estudiante("Carlos", "Pérez", 58)
estudiante3 = Estudiante("María", "Gómez", 92)


# Guardar los objetos en una lista
estudiantes = [
    estudiante1,
    estudiante2,
    estudiante3
]


# Mostrar todos los estudiantes
print("--- LISTADO DE ESTUDIANTES ---")

for estudiante in estudiantes:
    estudiante.mostrar_informacion()


# Guardar los estudiantes en un archivo
try:
    with open("calificaciones.txt", "w", encoding="utf-8") as archivo:

        for estudiante in estudiantes:
            linea = estudiante.convertir_a_texto()
            archivo.write(linea + "\n")

    print("Los estudiantes fueron guardados.")

except OSError:
    print("No fue posible escribir en el archivo.")