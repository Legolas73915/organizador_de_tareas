import json
import os

if os.path.exists('tareas.txt'):
    with open('tareas.txt', mode = 'r', encoding = 'utf-8' ) as tareas_file:
        tareas = json.load(tareas_file)
else:
    tareas = []

def guardar_tareas():
    with open('tareas.txt', mode = 'w', encoding = 'utf-8') as tareas_file:
        json.dump(tareas, tareas_file, ensure_ascii = False, indent = 4)

def estados():
    print("Estado: ")
    estado = None
    try:

        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            estado = "Pendiente"
        elif opcion == 2:
            estado = "En progreso"
        elif opcion == 3:
            estado = "Completada"
        else:
            estado = None
            print("Opcion invalida")
    except ValueError:
        print('Valor invalido')
    return estado


def agregar_tarea():
    print('Agregar tarea')
    titulo = input("Ingrese un titulo: ")
    titulo_existente = None
    for tarea in tareas:
        if titulo.lower() == tarea['titulo'].lower():
            titulo_existente = tarea
            break
    if titulo_existente:
        print("La tarea ya existe")
    else:
        descripcion = input("Ingrese un descripcion: ")
        prioridad = input("Ingrese un prioridad: ")
        print('1. Pendiente\n'
              '2. En progreso\n'
              '3. Completada')
        estado = estados()
        tarea = {'titulo': titulo, 'descripcion': descripcion, 'prioridad': prioridad, 'estado': estado}
        tareas.append(tarea)
        guardar_tareas()
        print('La tarea ha sido agregada')


def mostrar_tareas():
    if tareas == []:
        print('Lista vacia')
    else:
        print('Lista de tareas')
        for tarea in tareas:
            print(f'{tarea["titulo"]} \n'
                  f'{tarea["descripcion"]}\n'
                  f'{tarea["prioridad"]}\n'
                  f'{tarea["estado"]}\n')


def buscar_tarea():
    print('Buscar tarea')
    titulo = input("Ingrese un titulo: ")
    titulo_existente = False
    for tarea in tareas:
        if titulo.lower() == tarea['titulo'].lower():
            titulo_existente = tarea
            break
    if titulo_existente:
        print(f'{tarea["titulo"]} \n'
              f'{tarea["descripcion"]}\n'
              f'{tarea["prioridad"]}\n'
              f'{tarea["estado"]}')
    else:
        print('La tarea no existe')



def cambiar_estado():
    print('Cambiar estado:')
    titulo = input("Ingrese la tarea: ")
    estado = None
    for tarea in tareas:
        if titulo.lower() == tarea['titulo'].lower():
            estado = tarea['estado']
            break
    if estado:
        print('1. Pendiente\n'
              '2. En progreso\n'
              '3. Completada')
        estado = estados()
        tarea['estado'] = estado
        guardar_tareas()
        print('Estado actualizado')
    return estado









def eliminar_tarea():
    print('Eliminar tarea')
    titulo = input("Ingrese el titulo: ")
    titulo_existente = False
    for tarea in tareas:
        if titulo.lower() == tarea['titulo'].lower():
            titulo_existente = tarea
            break
    if titulo_existente:
        tareas.remove(titulo_existente)
        guardar_tareas()
        print('La tarea ha sido eliminada')
    else:
        print('La tarea no existe o ya ha sido eliminada')


def mostrar_tareas_pendientes():
    print('Tareas pendientes:')
    tareas_pendientes = False
    for tarea in tareas:
        if "estado" in tarea and tarea['estado'] == "Pendiente":
            print(f'{tarea["titulo"]} \n'
                  f'{tarea["descripcion"]}\n'
                  f'{tarea["prioridad"]}\n')
            tareas_pendientes = True
    if not tareas_pendientes:
        print('No hay tareas pendientes')


print('=====ORGANIZADOR DE TAREAS=====')
print('1. Agregar tarea\n'
      '2. Mostrar tareas\n'
      '3. Buscar tarea\n'
      '4. Cambiar estado\n'
      '5. Eliminar tarea\n'
      '6. Mostrar tareas pendientes\n'
      '7. Salir')


sesion = True
continuar = 0
while sesion:
    try:
        continuar = int(input("\nIngrese la opcion: "))
        if continuar == 1:
            agregar_tarea()
        elif continuar == 2:
            mostrar_tareas()
        elif continuar == 3:
            buscar_tarea()
        elif continuar == 4:
            cambiar_estado()
        elif continuar == 5:
            eliminar_tarea()
        elif continuar == 6:
            mostrar_tareas_pendientes()
        elif continuar == 7:
            print('Gracias por utilizar')
            sesion = False
    except ValueError:
        print('El valor es invalido')


