from estudiante import Estudiante
from facultad import Decano, Secretaria, Profesor


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

# ---------------------------------------------------------
# PERSONAL DE LA FACULTAD
# ---------------------------------------------------------
decano = Decano("Victor", "Vargas", "vvargas@facultad.edu.gt",
                "Facultad de Ingeniería", 2020)
secretaria = Secretaria("Laura", "Méndez", "lmendez@facultad.edu.gt",
                        "Lunes a Viernes 8:00 - 16:00")
profesor1 = Profesor("Jose", "Guerra", "jguerra@facultad.edu.gt",
                     "Programación")
profesor2 = Profesor("Sofía", "Castillo", "scastillo@facultad.edu.gt",
                     "Geología")

# El decano contrata profesores y se les asignan cursos
decano.contratar_profesor(profesor1)
decano.contratar_profesor(profesor2)
profesor1.asignar_curso("Programación I")
profesor1.asignar_curso("Estructuras de Datos")
profesor2.asignar_curso("Geología Aplicada")

print("\n--- PERSONAL DE LA FACULTAD ---")
decano.mostrar_informacion()
secretaria.mostrar_informacion()
profesor1.mostrar_informacion()
profesor2.mostrar_informacion()
# ---------------------------------------------------------
# SECRETARIA: registrar y consultar estudiantes
# ---------------------------------------------------------
print("\n--- SECRETARIA: REGISTRO ---")

for estudiante in estudiantes:
    if secretaria.registrar_estudiante(estudiante):
        print("Registrado:", estudiante.obtener_nombre_completo())

# Intentar registrar dos veces al mismo estudiante
if not secretaria.registrar_estudiante(estudiante1):
    print("Ana López ya estaba registrada (duplicado evitado).")

encontrado = secretaria.buscar_estudiante(estudiante2.id)
if encontrado is not None:
    print("Búsqueda por ID", estudiante2.id, "->", encontrado.obtener_nombre_completo())

print("Estudiantes que requieren seguimiento:")
for reprobado in secretaria.obtener_reprobados():
    print(" -", reprobado.obtener_nombre_completo(), "(", reprobado.nota, ")")
# ---------------------------------------------------------
# PROFESOR: calificar y analizar el rendimiento
# ---------------------------------------------------------
print("\n--- PROFESOR: CALIFICACIONES ---")

print("Promedio del grupo:", profesor1.calcular_promedio(estudiantes))

mejor = profesor1.obtener_mejor_estudiante(estudiantes)
print("Mejor estudiante:", mejor.obtener_nombre_completo(), "-", mejor.nota)

# Carlos entrega un trabajo de recuperación y se le corrige la nota
if profesor1.modificar_nota(estudiante2, 65):
    print("Nota de Carlos actualizada a:", estudiante2.nota,
          "->", estudiante2.obtener_estado())

# Intento de nota inválida
if not profesor1.modificar_nota(estudiante2, 150):
    print("Nota inválida rechazada (debe estar entre 0 y 100).")


# ---------------------------------------------------------
# DECANO: decisiones y resumen académico
# ---------------------------------------------------------
print("\n--- DECANO: RESUMEN ACADÉMICO ---")

resumen = decano.generar_resumen_academico(estudiantes)
print("Total de estudiantes:", resumen["total"])
print("Aprobados:", resumen["aprobados"])
print("Reprobados:", resumen["reprobados"])
print("Promedio general:", resumen["promedio"])
print("Porcentaje de aprobación:", resumen["porcentaje_aprobacion"], "%")

print("Candidatos a beca:")
for estudiante in estudiantes:
    if decano.aprobar_beca(estudiante):
        print(" -", estudiante.obtener_nombre_completo())


# Guardar los estudiantes en un archivo
try:
    with open("calificaciones.txt", "w", encoding="utf-8") as archivo:

        for estudiante in estudiantes:
            linea = estudiante.convertir_a_texto()
            archivo.write(linea + "\n")

    print("\nLos estudiantes fueron guardados.")

except OSError:
    print("No fue posible escribir en el archivo.")


# La secretaria genera el reporte oficial
if secretaria.generar_reporte("reporte_facultad.txt"):
    print("Reporte generado: reporte_facultad.txt")
else:
    print("No fue posible generar el reporte")    