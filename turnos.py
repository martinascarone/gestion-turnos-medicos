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

def modificarTurnos():
    dni = visualizarTurnos()
    #ingrese que turno le gustaria modificar
    #elimna el turno
    #aca lo mandaria al seleccione especialidad para que se agende el nuevo numero        
    
def visualizarTurnos():
 
    ruta_archivo = "db/turnos.csv"
    try:
        archivo = abrirArchivo(ruta_archivo,"rt")
        encabezados = archivo.readline().strip().split(',')
        
        if not encabezados or encabezados == ['']:
            archivo.close()
            archivo = abrirArchivo(ruta_archivo,"wt")
            archivo.write("dni,idProfesional,dia,hora,fecha\n")
            archivo.close()
            visualizarTurnos()

        turnos_encontrados = False
        contador = 1
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
    print("┌" + ("─"*4) + "┬" + ("─"*12) + "┬" + ("─"*10) + "┬" + ("─"*15) + "┐")
    print("│" + " " + "   " + "│" + " " + "Día" + " " * 8 + "│" + " " + "Horario" + "  " + "│" + " " + "Disponibilidad" +"│")
    print("├" + "─"*4 + "┼" + "─"*12 + "┼" + "─"*10 + "┼" + "─"*15 + "┤")

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
                return opciones[turnoSeleccionado]["dia"], opciones[turnoSeleccionado]["hora"], opciones[turnoSeleccionado]["fecha"]
        else:
            print("Debe ingresar un número válido.")

def eliminarTurno(): 
    dni = solicitarDNI()
    ruta_archivo = "db/turnos.csv"
    ruta_temp = "db/turnos_temp.csv"
    
    turno_encontrado = False
    
    try:
        archivo_original = open(ruta_archivo, "rt")
        archivo_temp = open(ruta_temp, "wt")
        
        #leer encabezados
        encabezados = archivo_original.readline()
        #print("Encab: ", encabezados)
        archivo_temp.write(encabezados)
        
        #leer linea por linea
        linea = archivo_original.readline()
        #print("Linea: ", linea)
        while linea:
            valores = linea.strip().split(',')
            if dni in valores:
                print(f"Turno encontrado")
                #TODO me tendria que dar el/los turnos encontrados
                #darme a elegir cual quiero seleccionar
                #borrar el seleecionado
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
    """finally:
        if archivo_original:
            archivo_original.close()
        if archivo_temp:
            archivo_temp.close()"""
                


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
