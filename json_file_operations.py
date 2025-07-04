# Escritura y lectura de archivos JSON en Python
import json


datos = {'Nombre': 'Juan', 'Edad': 25, 'Ciudad': 'Madrid'}


# Escritura de datos en un archivo JSON 
with open("datos.json", "w") as output_file: # Modos w: escribir,crear y truncar , w+ : leer, escribir y truncar  a: escribir y crear, a+: leer, escribir y crear  , r: leer, r+: leer y escribir 
    json.dump(datos, output_file, indent=4) # dump: escribir en el archivo, indent: indentar el archivo

# Lectura de datos desde un archivo JSON
with open("datos.json", "r") as file:
    datos = json.load(file)
# Observar que el archivo se crea en la misma carpeta que el archivo python
print(datos)

# Ahora vamos a trabajar con un archivo JSON con datos anidados 
datos = { 
    'persona': [
        {
            'nombre': 'Juan',
            'edad': 25,
            'ciudad': 'Madrid'
        },
        {
            'nombre': 'Maria',
            'edad': 30,
            'ciudad': 'Barcelona'
        }
    ]
}
# Escritura de datos anidados en un archivo JSON
with open("datos_anidados.json", "w") as output_file: 
    json.dump(datos, output_file, indent=4) 

# Lectura de datos anidados desde un archivo JSON
with open("datos_anidados.json", "r") as file:
    datos_anidados = json.load(file)
#Observar que los datos se cargan como un diccionario
print(datos_anidados)

#Ejemplo de como acceder a los datos anidados
print(datos_anidados['persona'][0]['nombre'])
print(datos_anidados['persona'][1]['nombre'])

#Ejemplo de como agregar un nuevo dato a los datos anidados
datos_anidados['persona'].append({'nombre': 'Pedro', 'edad': 40, 'ciudad': 'Valencia'})
#Escritura de datos anidados en un archivo JSON
with open("datos_anidados.json", "w") as output_file: 
    json.dump(datos_anidados, output_file, indent=4) 

#Ejemplo de como eliminar un dato de los datos anidados
datos_anidados['persona'].pop(0)
#Escritura de datos anidados en un archivo JSON
with open("datos_anidados.json", "w") as output_file: 
    json.dump(datos_anidados, output_file, indent=4) 

#Ejemplo de como modificar un dato de los datos anidados
datos_anidados['persona'][0]['nombre'] = 'Juan'
#Escritura de datos anidados en un archivo JSON
with open("datos_anidados.json", "w") as output_file: 
    json.dump(datos_anidados, output_file, indent=4) 
