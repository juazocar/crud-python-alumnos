def crear_alumno(alumnos):
    nombre  = input("Ingrese el nombre: ")
    edad    = input("Ingrese la edad: ")
    carrera = input("Ingrese la carrera: ")

    alumno = {
        "nombre": nombre,
        "edad": edad, 
        "carrera": carrera
    }

    alumnos.append(alumno)
    print("Alumno registrado correctamente. ")

def listar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
    else:
        print("=================================")
        print("---- SISTEMA CRUD DE ALUMNOS ----")
        print("=================================")
        
        for i, alumno in enumerate(alumnos):
            print("Id: ", i)
            print("Nombre: ", alumno["nombre"])
            print("Edad: ", alumno["edad"])
            print("Carrera: ", alumno["carrera"])
            print("-------------------------")

def actualizar_alumno(alumnos):
    listar_alumnos(alumnos)

    if len(alumnos) == 0:
        return

    try:
        id_alumno = int(input("Ingrese el ID del alumno a actualizar"))

        if id_alumno < 0 or id_alumno >= len(alumnos):
            print("Id inválido")
        else:
            nuevo_nombre  = input("Ingrese el nuevo nombre")
            nueva_edad    = input("Ingrese la nueva edad: ")
            nueva_carrera = input("Ingrese la nueva carrera: ")

            alumnos[id_alumno]["nombre"]  = nuevo_nombre
            alumnos[id_alumno]["edad"]    = nueva_edad
            alumnos[id_alumno]["carrera"] = nueva_carrera

            print("Alumno actualizado correctamente...")
    except:
        print("El ID del alumno debe ser un número entero mayor a cero") 

def eliminar_alumno(alumnos):
    listar_alumnos(alumnos)

    if len(alumnos) == 0:
        return
    try:
        id_alumno = int(input("Ingrese ID del alumno a eliminar"))

        if id_alumno < 0 or id_alumno >= len(alumnos):
            print("Id Inválido")
        else:
            alumnos.pop(id_alumno)
            print("Alumno eliminado correctamente")
    except:
        print("Debe ingresar un ID numérico válido.")
        
def guardar_alumnos(alumnos):
    with open("alumnos.txt", "w") as archivo:
        for alumno in alumnos:
            linea = alumno["nombre"]+","+alumno["edad"]+","+alumno["carrera"] + "\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")


def cargar_alumnos():
    alumnos = []

    try:
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                alumno = {
                    "nombre": datos[0],
                    "edad": datos[1],
                    "carrera": datos[2]
                }

                alumnos.append(alumno)

    except:
        print("No se encontró archivo previo. Se iniciará sin datos.")
    
    return alumnos
    
print("Se agrega nuevo texto")

alumnos = cargar_alumnos()

opcion = 0

while opcion != 6:
    print("--- Sistema CRUD de Alumnos ---")
    print("1. Registrar Alumno")
    print("2. Listar Alumnos")
    print("3. Actualizar Alumno")
    print("4. Eliminar Alumno")
    print("5. Guardar Datos")
    print("6. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            crear_alumno(alumnos)
        elif opcion == 2:
            listar_alumnos(alumnos)
        elif opcion == 3:
            actualizar_alumno(alumnos)
        elif opcion == 4:
            eliminar_alumno(alumnos)
        elif opcion == 5:
            guardar_alumnos(alumnos)
        elif opcion == 6:
            guardar_alumnos(alumnos)
            print("Programa finalizado")
        else:
            print("Opción no válida")

    except:
        print("Debe ingresar una opción numérica")
    