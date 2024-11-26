
def abrirArchivo(archivo,operacion):
    try:
        return open(archivo, operacion)
    except FileNotFoundError:
        nuevo_archivo = open(archivo, "wt")
        nuevo_archivo.close()
        return open(archivo, operacion)