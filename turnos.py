from json import JSONDecodeError
from especialidades import *
from inputs import *
from profesionales import *
from archivos import *

def modificarTurnos():
    dni = visualizarTurnos()
    #ingrese que turno le gustaria modificar
    #elimna el turno
    #aca lo mandaria al seleccione especialidad para que se agende el nuevo numero        
    
def visualizarTurnos():
    dni = solicitarDNI()
    ruta_archivo = "db/turnos.csv"
    try:
        archivo = abrirArchivo(ruta_archivo,"rt")
        encabezados = archivo.readline().strip().split(',')
        
        if not encabezados or encabezados == ['']:
            print("Archivo vacio")
            archivo.close()
            return

        turnos_encontrados = False
        contador = 1
        
        for linea in archivo:
            valores = linea.strip().split(',')
            registro = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            
            if dni in valores:
                dia = registro["dia"] if "dia" in registro else "no hay dia"
                hora = registro["hora"] if "hora" in registro else "no hay hora"
                print(f"{contador}) Tiene turno agendado para el dia {dia} a las {hora} hs.")
                
                turnos_encontrados = True
                contador += 1
        
        archivo.close()

        if turnos_encontrados:
            return dni  # Retorna el dni después de procesar todos los turnos
        else:
            print("No tiene turnos asociados")
            print("Volviendo al menú principal...")

    except FileNotFoundError:
        print("Error el archivo no se encontro")
    except Exception:
        print(f"Error inesperado")    

def reservarTurnos(profesionales):
    especialidadSeleccionada = 0 
    while True:
        especialidades = imprimirEspecialidades(profesionales)

        while True:
            try:
                especialidadSeleccionada = int(input("Ingrese el número de la especialidad que le interesa (o -1 para salir): ")) - 1

                if especialidadSeleccionada == -2:  # arreglamos indice
                    print("Finalizó Reserva.")
                    return

                if especialidadSeleccionada < -1 or especialidadSeleccionada >= len(especialidades):
                    print("Selección inválida. Por favor, seleccione un número válido.")
                    continue
                break  

            except ValueError:
                print("Error: Debe ingresar un número válido.")

        if especialidadSeleccionada == -2:  # arreglamos indice
            break
        
        #obtenemos la especialidad
        especialidadBuscada = especialidades[especialidadSeleccionada]
        imprimirProfesionales(profesionales, especialidadBuscada)

        #seleccionamos el profesional
        while True:
            try:
                profesionalSeleccionado = int(input("Ingrese el número del profesional que le interesa: ")) - 1

                if profesionalSeleccionado < 0 or profesionalSeleccionado >= len(especialidades):
                    print("Selección inválida. Por favor, seleccione un número válido.")
                    continue  
                break 

            except ValueError:
                print("Error: Debe ingresar un número válido.")

        dia, hora = imprimirTurnosDisponibles(profesionalSeleccionado + 1)

        guardarImprimirTurno(
            profesionalSeleccionado + 1,
            dia,
            hora,
            solicitarDatos()
        )
    pass

def isTurnoOcupado(dia, hora, idMedico):
    ARCHIVO_TURNOS = "db/turnos.csv"
    archivo_turnos = open(ARCHIVO_TURNOS, "rt")
    linea = archivo_turnos.readline() # lee el valor de la primer linea
    while linea != "": # Mientras el archivo no se haya terminado
        valores = linea.strip().split(',')
        if valores[3] == dia and int(valores[4]) == hora and int(valores[2]) == idMedico:
            # es el turno que estoy buscando
            return True
        else:
            # Lee la siguiente linea
            linea = archivo_turnos.readline()
    return False

def imprimirTurnosDisponibles(profesional):
    contador = 0
    opciones = []
    ARCHIVO_DISPONIBILIDADES = "db/disponibilidades.json"
    disponibilidades = abrirArchivo(ARCHIVO_DISPONIBILIDADES, "rt")
    disponibilidades = json.load(disponibilidades)
    print("┌" + ("─"*4) + "┬" + ("─"*12) + "┬" + ("─"*10) + "┬" + ("─"*15) + "┐")
    print("│" + " " + "   " + "│" + " " + "Día" + " " * 8 + "│" + " " + "Horario" + "  " + "│" + " " + "Disponibilidad" +"│")
    print("├" + "─"*4 + "┼" + "─"*12 + "┼" + "─"*10 + "┼" + "─"*15 + "┤")

    for turno in disponibilidades:
        if turno["idMedico"] == str(profesional):
            contadorHoras = int(turno["horarioSalida"]) - int(turno["horarioEntrada"])
            for hora in range(contadorHoras):
                dia = turno["dia"]
                hora_actual = int(turno["horarioEntrada"]) + hora
                ocupado = isTurnoOcupado(dia, hora_actual, profesional)
                opciones.append({
                    "dia": dia,
                    "hora": hora_actual,
                    "ocupado": ocupado
                })

                disponibilidad_texto = "OCUPADO" if ocupado else "DISPONIBLE"
                print(f"│ {contador + 1:<3}│ {dia:<10} │ {hora_actual:<8} │ {disponibilidad_texto:<13} │")
                contador += 1

    print("└" + "─"*4 + "┴" + "─"*12 + "┴" + "─"*10 + "┴" + "─"*15 + "┘")
    
    while True:
        turnoSeleccionado = input("Ingrese el número del turno que desea seleccionar: ")
        if turnoSeleccionado.isdigit():
            turnoSeleccionado = int(turnoSeleccionado) - 1
            if turnoSeleccionado < 0 or turnoSeleccionado >= len(opciones):
                print("Selección inválida. Por favor, seleccione un número válido.")
                continue
            if opciones[turnoSeleccionado]["ocupado"]:
                print("El turno seleccionado está ocupado. Por favor, seleccione otro turno.")
            else:
                return opciones[turnoSeleccionado]["dia"], opciones[turnoSeleccionado]["hora"]
        else:
            print("Debe ingresar un número válido.")

def eliminarTurno(): 
    dni = solicitarDNI()
    ruta_archivo = "db/turnos.csv"
    ruta_temp = "csv/turnos_temp.csv"
    
    turno_encontrado = False
    
    try:
        archivo_original = open(ruta_archivo, "rt", encoding="utf-8")
        archivo_temp = open(ruta_temp, "wt", encoding="utf-8")
        
        #leer encabezados
        encabezados = archivo_original.readline()
        print("Encab: ", encabezados)
        archivo_temp.write(encabezados)
        
        #leer linea por linea
        linea = archivo_original.readline()
        print("Linea: ", linea)
        while linea:
            valores = linea.strip().split(',')
            if dni in valores:
                print(f"Turno encontrado")
                turno_encontrado = True
                print("Eliminando turno...")
            else:
                archivo_temp.write(linea)
            linea = archivo_original.readline()
            
        if not turno_encontrado:
            print("No se encontraron turnos asociados al DNI ingresado.")
                
    
    except FileNotFoundError:
        print("El archivo de turnos no se encontró")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        if archivo_original:
            archivo_original.close()
        if archivo_temp:
            archivo_temp.close()
                


def guardarImprimirTurno(idProfesional, dia, hora, idPaciente):
    ARCHIVO_TURNOS = "db/turnos.csv"
    archivo_turnos = abrirArchivo(ARCHIVO_TURNOS,"wt")
    id = generarID()
    print(id)
    archivo_turnos.write(str(id) + ',' + str(idPaciente) + ',' + str(idProfesional) + ',' + dia + ',' + str(hora) + '\n')
    archivo_turnos.close()
    print("\n-------------------------------------------------" )
    print(f"Turno reservado para el día {dia} a las {hora}:00 hs")
    print("-------------------------------------------------\n" )

def generarID():
    ARCHIVO_ID_TURNOS = "db/idTurnos.json"
    try:
        archivo = abrirArchivo(ARCHIVO_ID_TURNOS,"rt")
        datos = json.load(archivo)
        id_actual = datos["id"]
        nuevo_id = id_actual + 1
        archivo.close()
    except (FileNotFoundError, KeyError, JSONDecodeError):
        nuevo_id = 1
        archivo = open(ARCHIVO_ID_TURNOS, 'wt')
        json.dump({"id":nuevo_id}, archivo)
        archivo.close()
        return 0