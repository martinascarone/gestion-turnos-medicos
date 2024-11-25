import json

def abrirArchivo(archivo,operacion):
    try:
        return open(archivo, operacion)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Creándolo...")
        nuevo_archivo = open(archivo, "wt")
        nuevo_archivo.close()
        return open(archivo, operacion)
    

def leer_pacientes():
    ruta_archivo = "db/pacientes.csv"
    try: #colocamos un try catch por si el archivo esta vacio
        archivo_pacientes = open(ruta_archivo, "rt")
        lineas = archivo_pacientes.readline()
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
    except IndexError:
        print(f"Error de índice al procesar el archivo")
        return []
    except Exception:
        print(f"Error inesperado")
        return []
