import json

def cargarJson(archivo):
    return json.load(open(archivo , "rt"))

def abrirArchivo(archivo):
    # Intenta abrir archivo, si no existe lo crea
    try:
        return open(archivo , "a")
    except OSError :
        return open(archivo , "x")
    

def leer_pacientes():
    ruta_archivo = "csv/pacientes.csv"
    try: #colocamos un try catch por si el archivo esta vacio
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo: 
            lineas = archivo.readlines()
        # Verificar si el archivo está vacío
        if not lineas:
            print("no hay registros almacenados")
            return []

        encabpacientes = lineas[0].strip().split(',') 
        pacientes = []

        for linea in lineas[1:]: 
            valores = linea.strip().split(',')
            registro = {encabpacientes[i]: valores[i] for i in range (len(encabpacientes))}
            pacientes.append(registro)
        print(pacientes)
        return pacientes
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return []
    except IndexError as e:
        print(f"Error de índice al procesar el archivo: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []
