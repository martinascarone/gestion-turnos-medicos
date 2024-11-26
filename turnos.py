from json import JSONDecodeError
from especialidades import *
from inputs import *
from profesionales import *
from archivos import *
from datetime import datetime, timedelta
import json

def proximo_dia_semana(dia_semana):
    if dia_semana < 1 or dia_semana > 7:
        raise ValueError("El día de la semana debe estar entre 1 (lunes) y 7 (domingo)")

    hoy = datetime.now()
    dia_actual = hoy.isoweekday()  # Devuelve el día actual (1 = lunes, 7 = domingo)
    dias_hasta_proximo = (dia_semana - dia_actual) % 7  # Calcular días hasta el próximo
    if dias_hasta_proximo == 0:
        dias_hasta_proximo = 7  # Si es hoy, cuenta hasta el próximo día de la misma semana

    proxima_fecha = hoy + timedelta(days=dias_hasta_proximo)
    return proxima_fecha.strftime("%d-%m-%Y")

def visualizarTurnos(dni):
 
    ruta_archivo = "db/turnos.csv"
    try:
        archivo = abrirArchivo(ruta_archivo,"rt")
        encabezados = archivo.readline().strip().split(',')
        
        if not encabezados or encabezados == ['']:
            archivo.close()
            archivo = abrirArchivo(ruta_archivo,"wt")
            archivo.write("dni,idProfesional,dia,hora,fecha\n")
            archivo.close()
            visualizarTurnos(dni)

        turnos_encontrados = False
        turnos_encontrados_lista = []
        contador = 1
        if not dni:
            dni = solicitarDNI()

        for linea in archivo:
            valores = linea.strip().split(',')
            registro = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            
            if dni in valores:
                dia = registro["dia"] if "dia" in registro else "no hay dia"
                hora = registro["hora"] if "hora" in registro else "no hay hora"
                fecha = registro["fecha"] if "fecha" in registro else "no hay fecha"
                print(f"{contador}) Tiene turno agendado para el dia {dia}({fecha}) a las {hora}hs.")
                turnos_encontrados = True
                turnos_encontrados_lista.append(registro)
                contador += 1
        
        archivo.close()

        if turnos_encontrados:
            return turnos_encontrados_lista  # Retorna el dni después de procesar todos los turnos
        else:
            print("No tiene turnos asociados")
            print("Volviendo al menú principal...")

    except FileNotFoundError:
        print("Error el archivo no se encontro")
    except Exception:
        print(f"Error inesperado")    

def reservarTurnos(profesionales):
    especialidadSeleccionada = 0 
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
        return
    
    #obtenemos la especialidad
    especialidadBuscada = especialidades[especialidadSeleccionada]
    cantProfesionales = imprimirProfesionales(profesionales, especialidadBuscada)

    #seleccionamos el profesional
    while True:
        try:
            profesionalSeleccionado = int(input("Ingrese el número del profesional que le interesa: "))

            if profesionalSeleccionado <= 0 or profesionalSeleccionado > cantProfesionales:
                print("Selección inválida. Por favor, seleccione un número válido.")
                continue  
            break 
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    dia, hora, fecha = imprimirTurnosDisponibles(profesionalSeleccionado)
    idProfesional = obtenerIdDeProfesional(profesionales,especialidadBuscada, profesionalSeleccionado)
    guardarImprimirTurno(
        idProfesional,
        dia,
        hora,
        fecha,
        solicitarDatos()
    )

def isTurnoOcupado(dia, hora, fecha, idMedico):
    ARCHIVO_TURNOS = "db/turnos.csv"
    archivo_turnos = open(ARCHIVO_TURNOS, "rt")
    linea = archivo_turnos.readline() # lee el valor de la primer linea
    while linea != "": # Mientras el archivo no se haya terminado
        valores = linea.strip().split(',')
        if valores[3] == dia and int(valores[4]) == hora and valores[5] == fecha  and int(valores[2]) == idMedico:
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
    print("┌" + ("─"*4) + "┬" + ("─"*12) + "┬" + ("─"*10) + "┬" + ("─"*15) + "┬" + ("─"*12) + "┐")
    print("│" + " " + "   " + "│" + " " + "Día" + " " * 8 + "│" + " " + "Horario" + "  " + "│" + " " + "Disponibilidad"+ "│" + " " + "Fecha" + "      " + "│" )
    print("├" + "─"*4 + "┼" + "─"*12 + "┼" + "─"*10 + "┼" + "─"*15 + "┼" + "─"*12 + "┤")

    for turno in disponibilidades:
        if turno["idMedico"] == str(profesional):
            contadorHoras = int(turno["horarioSalida"]) - int(turno["horarioEntrada"])
            for hora in range(contadorHoras):
                dia = turno["dia"]
                hora_actual = int(turno["horarioEntrada"]) + hora
                fecha = proximo_dia_semana(turno["isoday"])
                ocupado = isTurnoOcupado(dia, hora_actual, fecha, profesional)
                opciones.append({
                    "dia": dia,
                    "hora": hora_actual,
                    "ocupado": ocupado,
                    "fecha": fecha
                })

                disponibilidad_texto = "OCUPADO" if ocupado else "DISPONIBLE"
                print(f"│ {contador + 1:<3}│ {dia:<10} │ {hora_actual:<8} │ {disponibilidad_texto:<13} | { fecha } │")
                contador += 1

    print("└" + "─"*4 + "┴" + "─"*12 + "┴" + "─"*10 + "┴" + "─"*15 + "┴"+ "─"*12 + "┘")
    
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
                return opciones[turnoSeleccionado]["dia"], opciones[turnoSeleccionado]["hora"], opciones[turnoSeleccionado]["fecha"]
        else:
            print("Debe ingresar un número válido.")

def reprogramarTurno(): 
    dni = solicitarDNI()
    print("Seleccione el turno que desea reprogramar: ")
    turnos = visualizarTurnos(dni)
    turnoAReprogramarIndex = int(input("Ingrese el número del turno que desea reprogramar: "))
    if turnoAReprogramarIndex < 1 or turnoAReprogramarIndex > len(turnos):
        print("Selección inválida. Por favor, seleccione un número válido.")
        return
    
    turnoAReprogramar = turnos[turnoAReprogramarIndex - 1]
    ruta_archivo = "db/turnos.csv"
    turnosFinales = []
    archivo_original_lectura = open(ruta_archivo, "rt")

    for linea in archivo_original_lectura:
        valores = linea.strip().split(',')
        if turnoAReprogramar["dni"] in valores and turnoAReprogramar["idProfesional"] in valores and turnoAReprogramar["dia"] in valores and turnoAReprogramar["hora"] in valores and turnoAReprogramar["fecha"] in valores:
            print(f"Cancelando turno")
        else:
            turnosFinales.append(linea)
    archivo_original_lectura.close()
    archivo_original_escritura = open(ruta_archivo, "wt")
    for turno in turnosFinales:
        archivo_original_escritura.write(turno)
    archivo_original_escritura.close()


    dia, hora, fecha = imprimirTurnosDisponibles(turnoAReprogramar["idProfesional"])
    guardarImprimirTurno(
        turnoAReprogramar["idProfesional"],
        dia,
        hora,
        fecha,
        turnoAReprogramar["dni"]
    )


    print("Turno eliminado con éxito.")

def eliminarTurno(): 
    dni = solicitarDNI()
    print("Seleccione el turno que desea eliminar: ")
    turnos = visualizarTurnos(dni)
    turnoAEliminarIndex = int(input("Ingrese el número del turno que desea eliminar: "))
    if turnoAEliminarIndex < 1 or turnoAEliminarIndex > len(turnos):
        print("Selección inválida. Por favor, seleccione un número válido.")
        return
    
    turnoAEliminar = turnos[turnoAEliminarIndex - 1]
    ruta_archivo = "db/turnos.csv"
    turnosFinales = []
    archivo_original_lectura = open(ruta_archivo, "rt")

    for linea in archivo_original_lectura:
        valores = linea.strip().split(',')
        if turnoAEliminar["dni"] in valores and turnoAEliminar["idProfesional"] in valores and turnoAEliminar["dia"] in valores and turnoAEliminar["hora"] in valores and turnoAEliminar["fecha"] in valores:
            print(f"Eliminando turno")
        else:
            turnosFinales.append(linea)
    archivo_original_lectura.close()
    archivo_original_escritura = open(ruta_archivo, "wt")
    for turno in turnosFinales:
        archivo_original_escritura.write(turno)
    archivo_original_escritura.close()
    print("Turno eliminado con éxito.")

def guardarImprimirTurno(idProfesional, dia, hora, fecha ,idPaciente):
    # TODO: Implementar el campo fecha en el archivo de turnos
    # este campo debe ser la fecha calendario en la que se reservó el turno
    # Responsable: Joel Dias Correia
    ARCHIVO_TURNOS = "db/turnos.csv"
    archivo_turnos = abrirArchivo(ARCHIVO_TURNOS,"at")
    archivo_turnos.write(str(idPaciente) + ',' + str(idProfesional) + ',' + dia + ',' + str(hora) + ',' + fecha + '\n')
    archivo_turnos.close()
    print("\n-------------------------------------------------" )
    print(f"Turno reservado para el día {dia}({fecha}) a las {hora}:00 hs.")
    print("-------------------------------------------------\n" )
