from especialidades import *
from inputs import *
from profesionales import *
from archivos import *
import random

def modificarTurnos():
    dni = visualizarTurnos()
    #ingrese que turno le gustaria modificar
    #elimna el turno
    #aca lo mandaria al seleccione especialidad para que se agende el nuevo numero        
    
def visualizarTurnos():
    dni = solicitarDNI()
    ruta_archivo = "csv/turnos.csv"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            encabezados = archivo.readline().strip().split(',')
            
            if not encabezados or encabezados == ['']:
                print("Archivo vacio")
                return

            turnos_encontrados = False
            contador = 1
            
            for linea in archivo:
                valores = linea.strip().split(',')
                registro = {encabezados[i]: valores[i] for i in range(len(encabezados))} #diccionario con el registro
                
                if dni in valores:
                    dia = registro["dia"] if "dia" in registro else "no hay dia"
                    hora = registro["hora"] if "hora" in registro else "no hay hora"
                    print(f"{contador}) Tiene turno agendado para el dia {dia} a las {hora} hs.")
                    
                    turnos_encontrados = True
                    contador += 1
            if turnos_encontrados:
                return dni  # Retorna el dni después de procesar todos los turnos
            else:
                print("No tiene turnos asociados")
                print("Volviendo al menu principal...")

    except FileNotFoundError:
        print("Error el archivo no se encontro")
    except Exception as e:
        print(f"Error inesperado: {e}")
        

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
    archivo_turnos = open(ARCHIVO_TURNOS, 'r', encoding='utf-8')
    lineas = archivo_turnos.readlines()
    for linea in lineas:
        valores = linea.strip().split(',')
        if valores[3] == dia and int(valores[4]) == hora and int(valores[2]) == idMedico:
            return True
    return False

def imprimirTurnosDisponibles(profesional):
    contador = 0
    opciones = []
    ARCHIVO_DISPONIBILIDADES = "db/disponibilidades.json"
    disponibilidades = cargarJson(ARCHIVO_DISPONIBILIDADES)

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

# def eliminarTurno(): 
    # TODO Implementar la eliminación de un turno
    # Responsable: Martina Scarone


def guardarImprimirTurno(idProfesional, dia, hora, idPaciente):
    # TODO: Implementar el campo fecha en el archivo de turnos
    # este campo debe ser la fecha calendario en la que se reservó el turno
    # Responsable: Joel Dias Correia
    ARCHIVO_TURNOS = "db/turnos.csv"
    archivo_turnos = abrirArchivo(ARCHIVO_TURNOS)
    id = random.randint(1, 10000) # TODO: Eliminar esta línea, debe ser reemplzada por un contador de turnos
    archivo_turnos.write(str(id) + ',' + str(idPaciente) + ',' + str(idProfesional) + ',' + dia + ',' + str(hora) + '\n')
    archivo_turnos.close()
    print("\n-------------------------------------------------" )
    print(f"Turno reservado para el día {dia} a las {hora}:00 hs")
    print("-------------------------------------------------\n" )

def contadorDeturnos():
    # TODO: Implementar un contador de turnos
    # para esto se debe leer el archivo de turnos y contar cuantos turnos hay
    # y devolver el valor del contador
    # Y borrar la linea que genera un id random en la funcion guardarImprimirTurno
    # Responsable: Zoe Preiti Tasat
    return 0