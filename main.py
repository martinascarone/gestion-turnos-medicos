import random

profesionales =[
    {
        "id": "1",
        "nombre": "Carlos",
        "apellido": "Maslaton",
        "especialidad": "Oftalmologo",
    },
    {
        "id": "2",
        "nombre": "Juan",
        "apellido": "Rodriguez",
        "especialidad": "Oftalmologo",
    },
    {
        "id": "3",
        "nombre": "Carla",
        "apellido": "Gomez",
        "especialidad": "Pediatra",
    },
    {
        "id": "4",
        "nombre": "Martina",
        "apellido": "Quintana",
        "especialidad": "Nutricionista",
    },
    {
        "id": "5",
        "nombre": "Jorge",
        "apellido": "Bisbal",
        "especialidad": "Pediatra",
    },
    {
        "id": "6",
        "nombre": "Laura",
        "apellido": "Perez",
        "especialidad": "Oftalmologo",
    },
    {
        "id": "7",
        "nombre": "Mariana",
        "apellido": "Isola",
        "especialidad": "Nutricionista",
    }
]

disponibilidades = [
    {
        "id": "1",
        "idMedico": "1",
        "dia": "Lunes",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "2",
        "idMedico": "1",
        "dia": "Miércoles",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "2",
        "idMedico": "1",
        "dia": "Jueves",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "3",
        "idMedico": "2",
        "dia": "Martes",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "4",
        "idMedico": "2",
        "dia": "Viernes",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "5",
        "idMedico": "2",
        "dia": "Sábado",
        "horarioEntrada": 13,
        "horarioSalida": 17,
    },
    {
        "id": "6",
        "idMedico": "3",
        "dia": "Lunes",
        "horarioEntrada": 10,
        "horarioSalida": 13,
    },
    {
        "id": "7",
        "idMedico": "3",
        "dia": "Martes",
        "horarioEntrada": 14,
        "horarioSalida": 18,
    },
    {
        "id": "8",
        "idMedico": "4",
        "dia": "Jueves",
        "horarioEntrada": 9,
        "horarioSalida": 13,
    },
    {
        "id": "9",
        "idMedico": "4",
        "dia": "Lunes",
        "horarioEntrada": 10,
        "horarioSalida": 13,
    },
    {
        "id": "10",
        "idMedico": "4",
        "dia": "Miércoles",
        "horarioEntrada": 10,
        "horarioSalida": 12,
    },
    {
        "id": "11",
        "idMedico": "5",
        "dia": "Martes",
        "horarioEntrada": 9,
        "horarioSalida": 12,
    },
    {
        "id": "12",
        "idMedico": "5",
        "dia": "Jueves",
        "horarioEntrada": 14,
        "horarioSalida": 17,
    },
    {
        "id": "13",
        "idMedico": "6",
        "dia": "Viernes",
        "horarioEntrada": 9,
        "horarioSalida": 13,
    },
    {
        "id": "14",
        "idMedico": "7",
        "dia": "Viernes",
        "horarioEntrada": 10,
        "horarioSalida": 13,
    },
    {
        "id": "15",
        "idMedico": "8",
        "dia": "Sábado",
        "horarioEntrada": 10,
        "horarioSalida": 12,
    }
]

turnos = [
    {'id': '1', 'idPaciente': 1, 'idMedico': 2, 'dia': 'Martes', 'hora': 13}
    # {
    #     "id": "1",
    #     "idPaciente": "1",
    #     "idMedico": "1",
    #     "dia": "Lunes",
    #     "hora": "13:00",
    # }
]

pacientes = [
    # {
    #     "id": "1",
    #     "nombre": "Juan",
    #     "apellido": "Perez",
    #     "dni": "12345678",
    # }
]

def isTurnoOcupado(dia, hora, idMedico):
    # hay que mejorarla
    for turno in turnos:
        if turno["dia"] == dia and turno["hora"] == hora and turno["idMedico"] == str(idMedico):
            return True
    return False

def imprimirTurnosDisponibles(profesional):
    contador = 0
    disponibles = []
    for turno in disponibilidades:
        if turno["idMedico"] == str(profesional):
            contadorHoras = turno["horarioSalida"] - turno["horarioEntrada"]
            for hora in range(contadorHoras):
                hora_actual = turno["horarioEntrada"] + hora
                if(isTurnoOcupado(turno["dia"], hora_actual, profesional)):
                    print(contador + 1, ")", turno["dia"], hora_actual, "hs OCUPADO")
                else:
                    disponibles.append((turno["dia"], hora_actual))  # Almacena una tupla (día, hora)
                    print(contador + 1, ")", turno["dia"], hora_actual, "hs")
                contador += 1

    turnoSeleccionado = int(input("Ingrese el número del turno que desea seleccionar: ")) - 1
    return disponibles[turnoSeleccionado]  # Retorna una tupla (día, hora)

            
def seleccionarTurno(idTurno, dia, hora,paciente):
    turnos.append(
        {
            "id": str(len(turnos) + 1),
            "idPaciente": paciente,
            "idMedico": idTurno,
            "dia": dia,
            "hora": hora
        }
    )
'''
 - Funcion original para generar la lista de turnos sin duplicados -
def generarListaEspecialidades(lista):
    #ingresa lista de diccionarios con datos de profesionales, sale listado de especialidades sin duplicados
    
    listaEspecialidades = []
    for profesional in lista:
        especialidad = profesional["especialidad"]
        if especialidad not in listaEspecialidades:
            listaEspecialidades.append(especialidad)
    return listaEspecialidades'''

#Funcion lambda para generar la lista de turnos sin duplicados
generarListaEspecialidades = lambda lista: list(set(map(lambda p: p["especialidad"], lista)))


def imprimirEspecialidades(lista):
    especialidades = generarListaEspecialidades(lista)
    indice = 0
    print("Hola! ¿Qué especialidad estás buscando?")
    while indice < len(especialidades):
        print(indice + 1, ")", especialidades[indice])
        indice += 1
    print("-1) Finalizar")
    return especialidades

'''
 - Funcion original para generar lista de profesionales asosiados a la especialidad -

def generarListaProfesionales(lista, especialidadBuscada):
    """
    mostrar profesionales disponibles de la especialidad seleccionada
    """
    listaProfesionales = []
    for profesional in lista:
        if especialidadBuscada == profesional["especialidad"]:
            listaProfesionales.append(profesional)
    return listaProfesionales
'''
#funcion lamda para generar lista de profesionales asosciados a la especialidad seleccionada
generarListaProfesionales = lambda lista, especialidadBuscada: list(filter(lambda p: p["especialidad"] == especialidadBuscada, lista))



def imprimirProfesionales(lista, especialidadBuscada):
    profesionales = generarListaProfesionales(lista, especialidadBuscada)
    indice = 0
    while indice < len(profesionales):
        print(indice + 1, ")", profesionales[indice]["nombre"], profesionales[indice]["apellido"])
        indice += 1
    print("Seleccione el Profesional que desea consultar")
    print("-1) Finalizar")


# def mostrarTurnoMedico(matriz):
#     datosPaciente = solicitarDatos(matriz)
#     print("------------------------")
#     print(f"Hola!{nombre},{apellido}")

#Creamos una matriz de diccionarios para poder acceder a los daos de los profecionales de forma sencilla


"""Horarios asignados:
Carlos Maslaton (Oftalmologo):
    Lunes: 13:00 - 17:00
    Miércoles: 13:00 - 17:00
    Jueves: 13:00 - 17:00

Juan Rodriguez (Oftalmologo):
    Martes: 13:00 - 17:00
    Viernes: 13:00 - 17:00
    Sábado: 13:00 - 17:00

Carla Gomez (Pediatra):
    Lunes: 10:00 - 13:00
    Martes: 14:00 - 18:00
    Jueves: 9:00 - 13:00

Martina Quintana (Nutricionista):
    Lunes: 10:00 - 13:00
    Miércoles: 10:00 - 12:00

Jorge Bisbal (Pediatra):
    Martes: 9:00 - 12:00
    Jueves: 14:00 - 17:00

Laura Perez (Oftalmologo):
    Viernes: 9:00 - 13:00"""

"""
ingresar profesional, ingresar paciente, mostrar dias disponibles, mostrar horarios disponibles, seleccionar uno, almacenar en pacientes. 

"""
#Inicio Peograma
"""crear funcion que muestre las fechas disponibles de cada medico!!!!!!!!
decir cual es el trno libre mas proximo"""

#pacienteMatriz = [nombre, apellido, dni, id]

#generarListaEspecialidades(matriz)
#imprimirDatos(matriz)


def solicitarDatos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = int(input("Ingrese su DNI: "))
    dni = int(dni)
    id = len(pacientes) + 1
    pacientes.append([id, nombre, apellido, dni])
    return id

# Inicio Programa
especialidadSeleccionada = 0 

while especialidadSeleccionada != -1:
    especialidades = imprimirEspecialidades(profesionales)
    especialidadSeleccionada = int(input("Ingrese el número de la especialidad que le interesa (o -1 para salir): ")) - 1
    
    if especialidadSeleccionada == -2:  # Cuando el usuario selecciona -1
        print("Finalizó Reserva.")
        break
    
    especialidadBuscada = especialidades[especialidadSeleccionada]
    imprimirProfesionales(profesionales, especialidadBuscada)
    
    profesionalSeleccionado = int(input("Ingrese el número del profesional que le interesa: ")) - 1
    dia, hora = imprimirTurnosDisponibles(profesionalSeleccionado + 1)


    seleccionarTurno(
        profesionalSeleccionado + 1,
        dia,
        hora,
        solicitarDatos()
    )

    print("PROFESIONALES", profesionales)
    print("TURNOS", turnos)
    print("PACIENTES", pacientes)
