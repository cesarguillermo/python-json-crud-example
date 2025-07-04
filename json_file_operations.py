"""
json_file_operations.py

Ejemplo simple de operaciones CRUD con archivos JSON en Python.
"""

import json


def escribir_json_simple():
    """Escribe datos simples en un archivo JSON."""
    datos = {'Nombre': 'Juan', 'Edad': 25, 'Ciudad': 'Madrid'}
    with open("datos.json", "w") as output_file:
        json.dump(datos, output_file, indent=4)


def leer_json_simple():
    """Lee datos simples desde un archivo JSON."""
    with open("datos.json", "r") as file:
        datos = json.load(file)
    print("Datos simples:", datos)


def escribir_json_anidado():
    """Escribe datos anidados en un archivo JSON."""
    datos = {
        'persona': [
            {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'},
            {'nombre': 'Maria', 'edad': 30, 'ciudad': 'Barcelona'}
        ]
    }
    with open("datos_anidados.json", "w") as output_file:
        json.dump(datos, output_file, indent=4)


def leer_json_anidado():
    """Lee datos anidados desde un archivo JSON."""
    with open("datos_anidados.json", "r") as file:
        datos_anidados = json.load(file)
    print("Datos anidados:", datos_anidados)
    return datos_anidados


def mostrar_nombres(datos):
    """Muestra los nombres de las personas."""
    for i, persona in enumerate(datos['persona']):
        print(f"Persona {i+1}: {persona['nombre']}")


def agregar_persona(datos, nombre, edad, ciudad):
    """Agrega una nueva persona a los datos anidados."""
    datos['persona'].append({'nombre': nombre, 'edad': edad, 'ciudad': ciudad})


def eliminar_persona(datos, indice):
    """Elimina una persona según el índice."""
    if 0 <= indice < len(datos['persona']):
        datos['persona'].pop(indice)


def modificar_nombre(datos, indice, nuevo_nombre):
    """Modifica el nombre de una persona según el índice."""
    if 0 <= indice < len(datos['persona']):
        datos['persona'][indice]['nombre'] = nuevo_nombre


def guardar_datos(datos, archivo):
    """Guarda los datos en un archivo JSON."""
    with open(archivo, "w") as output_file:
        json.dump(datos, output_file, indent=4)


if __name__ == "__main__":
    # Parte 1: Datos simples
    escribir_json_simple()
    leer_json_simple()

    # Parte 2: Datos anidados
    escribir_json_anidado()
    datos = leer_json_anidado()
    mostrar_nombres(datos)

    # CRUD sobre datos anidados
    agregar_persona(datos, 'Pedro', 40, 'Valencia')
    eliminar_persona(datos, 0)
    modificar_nombre(datos, 0, 'Juan')
    guardar_datos(datos, "datos_anidados.json")
