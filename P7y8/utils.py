import json
from excepciones import ErrorArchivo
from publicacion import Libro, Revista

def validar_cadena(cadena):
    if not cadena or not isinstance(cadena, str):
        raise ValueError("El valor debe ser una cadena no vacía.")
    return cadena

def validar_entero(valor):
    if not isinstance(valor, int) or valor <= 0:
        raise ValueError("El valor debe ser un entero positivo.")
    return valor

def guardar_publicaciones(nombre_archivo, publicaciones):
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump([pub.__dict__ for pub in publicaciones], archivo)
    except Exception as e:
        raise ErrorArchivo(f"Error al guardar publicaciones: {e}")

def cargar_publicaciones(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            publicaciones = []
            for dato in datos:
                if '_genero' in dato:
                    publicaciones.append(Libro(dato['_titulo'], dato['_autor'], dato['_anio'], dato['_genero']))
                elif '_num_edicion' in dato:
                    publicaciones.append(Revista(dato['_titulo'], dato['_autor'], dato['_anio'], dato['_num_edicion']))
            return publicaciones
    except FileNotFoundError:
        raise ErrorArchivo("El archivo no existe.")
    except Exception as e:
        raise ErrorArchivo(f"Error al cargar publicaciones: {e}")
