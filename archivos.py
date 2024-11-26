
def abrirArchivo(archivo,operacion):
    try:
        return open(archivo, operacion)
    except FileNotFoundError:
        nuevo_archivo = open(archivo, "wt")
        nuevo_archivo.close()
        return open(archivo, operacion)
    
def crearArchTurnos():
    ruta_archivo = "db/turnos.csv"
    try:
        archivo = open(ruta_archivo, "wt")
        archivo.write("dni,idProfesional,dia,hora,fecha\n")
        archivo.close
        print("turnos.csv creado")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
        
def crearArchPacientes():
    ruta_archivo = "db/pacientes.csv"
    try:
        archivo = open(ruta_archivo, "wt")
        archivo.write("dni,nombre,apellido\n")
        archivo.close
        print("pacientes.csv creado")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")