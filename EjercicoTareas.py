tareas = []

def mostrarTareas():
    if not tareas:
        print("No tienes tareas pendientes")
    else:
        for x,y in enumerate(tareas):
            print(f"{x}.- {y}")

def crearTarea():
    tarea = input("Escribe la tarea que quieres agregar: ")
    tareas.append(tarea)
    print("tarea agregada")

def borrarTarea():
    for indice, valor in enumerate(tareas):
        print(f"{indice} - {valor}")

    eleccion= int(input("Seleccione que tarea desea eliminar: "))
    if eleccion > len(tareas)-1:
        print("El numero de tarea no existe")
    elif eleccion < 0:
        print("El numero de tarea no existe")
    else:
        tareas.remove(tareas[eleccion])
        print("Tarea Eliminada.")

while True:
    print("\nOpciones:")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        mostrarTareas()
    elif opcion == '2':
        crearTarea()
    elif opcion == '3':
        borrarTarea()
    elif opcion == '4':
        break
    else:
        print("Opción no válida.")

