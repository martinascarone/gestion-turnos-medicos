
ARCHIVO_PACIENTE = "db/pacientes.csv"
ARCHIVO_TURNOS = "db/turnos.csv"

def abrirArchivo(archivo,operacion):
    try:
        return open(archivo, operacion)
    except FileNotFoundError:
        nuevo_archivo = open(archivo, "wt")
        nuevo_archivo.close()
        return open(archivo, operacion)
    
def crearArchTurnos():
    try:
        archivo = open(ARCHIVO_TURNOS, "wt")
        archivo.write("dni,idProfesional,dia,hora,fecha\n")
        archivo.close()
    except Exception:
        print(f"Error al crear el archivo")
        
def crearArchPacientes():
    try:
        archivo = open(ARCHIVO_PACIENTE, "wt")
        archivo.close()
    except Exception:
        print(f"Error al crear el archivo")

def verificarExistenciaArchivoTurnos():
    try:
        archivo = open(ARCHIVO_TURNOS, "rt")
        archivo.close()
    except FileNotFoundError:
        crearArchTurnos()

def verificarExistenciaArchivoPacientes():
    try:
        archivo = open(ARCHIVO_PACIENTE, "rt")
        archivo.close()
    except FileNotFoundError:
        crearArchPacientes()