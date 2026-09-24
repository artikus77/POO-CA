import random


class Persona:
    """
    Clase base con los datos comunes del personal de la facultad.
    Decano, Secretaria y Profesor heredan de ella.
    """

    def __init__(self, nombre, apellido, correo):
        self.id = random.randint(1000, 9999)
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido

    def mostrar_informacion(self):
        print("ID:", self.id)
        print("Nombre:", self.obtener_nombre_completo())
        print("Correo:", self.correo)

    def convertir_a_texto(self):
        return (
            str(self.id) + "," +
            self.nombre + "," +
            self.apellido + "," +
            self.correo
        )


class Decano(Persona):
    """
    Autoridad máxima de la facultad. Administra a los profesores
    y toma decisiones académicas sobre los estudiantes.
    """

    def __init__(self, nombre, apellido, correo, facultad, anio_inicio):
        super().__init__(nombre, apellido, correo)
        self.facultad = facultad
        self.anio_inicio = anio_inicio
        self.profesores = []

    def contratar_profesor(self, profesor):
        """Agrega un profesor a la facultad (sin duplicados)."""
        if profesor in self.profesores:
            return False
        self.profesores.append(profesor)
        return True

    def aprobar_beca(self, estudiante, nota_minima=85):
        """Un estudiante califica para beca si su nota alcanza el mínimo."""
        return estudiante.nota >= nota_minima

    def generar_resumen_academico(self, estudiantes):
        """Devuelve estadísticas generales de la facultad."""
        if len(estudiantes) == 0:
            return None

        aprobados = 0
        suma = 0
        for estudiante in estudiantes:
            suma += estudiante.nota
            if estudiante.obtener_estado() == "Aprobado":
                aprobados += 1

        total = len(estudiantes)
        return {
            "total": total,
            "aprobados": aprobados,
            "reprobados": total - aprobados,
            "promedio": round(suma / total, 2),
            "porcentaje_aprobacion": round(aprobados / total * 100, 1),
        }

    def mostrar_informacion(self):
        print("=== DECANO ===")
        super().mostrar_informacion()
        print("Facultad:", self.facultad)
        print("En el cargo desde:", self.anio_inicio)
        print("Profesores a cargo:", len(self.profesores))
        print("-------------------------")


class Secretaria(Persona):
    """
    Encargada de la parte administrativa: registra estudiantes,
    los busca y genera reportes.
    """

    def __init__(self, nombre, apellido, correo, horario):
        super().__init__(nombre, apellido, correo)
        self.horario = horario
        self.estudiantes_registrados = []

    def registrar_estudiante(self, estudiante):
        """Registra un estudiante si su ID aún no existe."""
        if self.buscar_estudiante(estudiante.id) is not None:
            return False
        self.estudiantes_registrados.append(estudiante)
        return True

    def buscar_estudiante(self, id_estudiante):
        """Busca un estudiante por su ID. Devuelve None si no existe."""
        for estudiante in self.estudiantes_registrados:
            if estudiante.id == id_estudiante:
                return estudiante
        return None

    def obtener_reprobados(self):
        """Lista de estudiantes que necesitan seguimiento."""
        reprobados = []
        for estudiante in self.estudiantes_registrados:
            if estudiante.obtener_estado() == "Reprobado":
                reprobados.append(estudiante)
        return reprobados

    def generar_reporte(self, nombre_archivo):
        """Escribe un reporte de todos los estudiantes registrados."""
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("REPORTE DE ESTUDIANTES\n")
                archivo.write("Elaborado por: " + self.obtener_nombre_completo() + "\n\n")

                for estudiante in self.estudiantes_registrados:
                    archivo.write(
                        str(estudiante.id) + " | " +
                        estudiante.obtener_nombre_completo() + " | " +
                        str(estudiante.nota) + " | " +
                        estudiante.obtener_estado() + "\n"
                    )
            return True
        except OSError:
            return False

    def mostrar_informacion(self):
        print("=== SECRETARIA ===")
        super().mostrar_informacion()
        print("Horario:", self.horario)
        print("Estudiantes registrados:", len(self.estudiantes_registrados))
        print("-------------------------")


class Profesor(Persona):
    """
    Imparte cursos, califica y analiza el rendimiento de sus estudiantes.
    """

    def __init__(self, nombre, apellido, correo, especialidad):
        super().__init__(nombre, apellido, correo)
        self.especialidad = especialidad
        self.cursos = []

    def asignar_curso(self, curso):
        if curso in self.cursos:
            return False
        self.cursos.append(curso)
        return True

    def modificar_nota(self, estudiante, nueva_nota):
        """Cambia la nota de un estudiante; solo acepta valores de 0 a 100."""
        if nueva_nota < 0 or nueva_nota > 100:
            return False
        estudiante.nota = nueva_nota
        return True

    def calcular_promedio(self, estudiantes):
        """Promedio de notas de un grupo de estudiantes."""
        if len(estudiantes) == 0:
            return 0
        suma = 0
        for estudiante in estudiantes:
            suma += estudiante.nota
        return round(suma / len(estudiantes), 2)

    def obtener_mejor_estudiante(self, estudiantes):
        """Devuelve el estudiante con la nota más alta."""
        if len(estudiantes) == 0:
            return None
        mejor = estudiantes[0]
        for estudiante in estudiantes:
            if estudiante.nota > mejor.nota:
                mejor = estudiante
        return mejor

    def mostrar_informacion(self):
        print("=== PROFESOR ===")
        super().mostrar_informacion()
        print("Especialidad:", self.especialidad)
        print("Cursos:", ", ".join(self.cursos) if self.cursos else "Sin cursos")
        print("-------------------------")
