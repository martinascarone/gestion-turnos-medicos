import random

def generarListaEspecialidades(lista):
    '''
    ingresa lista de diccionarios con datos de profesionales, sale listado de especialidades sin duplicados
    '''
    listaEspecialidades = []
    for profesional in lista:
        especialidad = profesional["especialidad"]
        if especialidad not in listaEspecialidades:
            listaEspecialidades.append(especialidad)
    return listaEspecialidades


def imprimirEspecialidades(lista):
    especialidades = generarListaEspecialidades(lista)
    indice = 0
    print("Hola! ¿Qué especialidad estás buscando?")
    while indice < len(especialidades):
        print(indice + 1, ")", especialidades[indice])
        indice += 1
    print("-1) Finalizar")
    return especialidades


def generarListaProfesionales(lista, especialidadBuscada):
    """
    mostrar profesionales disponibles de la especialidad seleccionada
    """
    listaProfesionales = []
    for profesional in lista:
        if especialidadBuscada == profesional["especialidad"]:
            listaProfesionales.append(profesional)
    return listaProfesionales


def imprimirProfesionales(lista, especialidadBuscada):
    profesionales = generarListaProfesionales(lista, especialidadBuscada)
    indice = 0
    while indice < len(profesionales):
        print(indice + 1, ")", profesionales[indice]["apellido"])
        indice += 1
    print("-1) Finalizar")

"""
def mostrarDisponibilidad(matriz):
    #mostrar dias disponibles     mostrar horarios disponibles


def solicitarDatos(matriz):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = int(input("Ingrese su DNI: "))
    dni = int(dni)
    id = random.randint(1, 1000)
    pacienteMatriz.append(["id", "nombre", "apellido", "dni"])
    print(pacienteMatriz)
    return pacienteMatriz

def mostrarTurnoMedico(matriz)
    datosPaciente = solicitarDatos(matriz)
    print("------------------------")
    print(f"Hola!{nombre},{apellido}")

"""

#Creamos una matriz de diccionarios para poder acceder a los daos de los profecionales de forma sencilla
profesionales = [
    {"ID": "1", "nombre": "Carlos", "apellido": "Maslaton", "especialidad": "Oftalmologo", 
     "disponibilidad": [
        {"dia": "Lunes", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                      {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}]},
        {"dia": "Miercoles", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                          {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}]},
        {"dia": "Jueves", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                       {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}]}]},
    
    {"ID": "2", "nombre": "Juan", "apellido": "Rodriguez", "especialidad": "Oftalmologo", 
     "disponibilidad": [
        {"dia": "Martes", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                        {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}, 
                                        {"hora": 17, "reservado": False}]},
        {"dia": "Viernes", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                        {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}, 
                                        {"hora": 17, "reservado": False}]},
        {"dia": "Sábado", "horarios": [{"hora": 13, "reservado": False}, {"hora": 14, "reservado": False}, 
                                        {"hora": 15, "reservado": False}, {"hora": 16, "reservado": False}, 
                                        {"hora": 17, "reservado": False}]}]},
    
    {"ID": "3", "nombre": "Carla", "apellido": "Gomez", "especialidad": "Pediatra", 
     "disponibilidad": [
        {"dia": "Lunes", "horarios": [{"hora": 10, "reservado": False}, {"hora": 11, "reservado": False}, 
                                      {"hora": 12, "reservado": False}, {"hora": 13, "reservado": False}]},
        {"dia": "Martes", "horarios": [{"hora": 14, "reservado": False}, {"hora": 15, "reservado": False}, 
                                       {"hora": 16, "reservado": False}, {"hora": 17, "reservado": False}, 
                                       {"hora": 18, "reservado": False}]},
        {"dia": "Jueves", "horarios": [{"hora": 9, "reservado": False}, {"hora": 10, "reservado": False}, 
                                       {"hora": 11, "reservado": False}, {"hora": 12, "reservado": False}, 
                                       {"hora": 13, "reservado": False}]}]},

    {"ID": "4", "nombre": "Martina", "apellido": "Quintana", "especialidad": "Nutricionista", 
     "disponibilidad": [
        {"dia": "Lunes", "horarios": [{"hora": 10, "reservado": False}, {"hora": 11, "reservado": False}, 
                                      {"hora": 12, "reservado": False}, {"hora": 13, "reservado": False}]},
        {"dia": "Miercoles", "horarios": [{"hora": 10, "reservado": False}, {"hora": 11, "reservado": False}, 
                                          {"hora": 12, "reservado": False}]}]},
    
    {"ID": "5", "nombre": "Jorge", "apellido": "Bisbal", "especialidad": "Pediatra", 
     "disponibilidad": [
        {"dia": "Martes", "horarios": [{"hora": 9, "reservado": False}, {"hora": 10, "reservado": False}, 
                                       {"hora": 11, "reservado": False}, {"hora": 12, "reservado": False}]},
        {"dia": "Jueves", "horarios": [{"hora": 14, "reservado": False}, {"hora": 15, "reservado": False}, 
                                       {"hora": 16, "reservado": False}, {"hora": 17, "reservado": False}]}]},

    {"ID": "6", "nombre": "Laura", "apellido": "Perez", "especialidad": "Oftalmologo", 
     "disponibilidad": [
        {"dia": "Viernes", "horarios": [{"hora": 9, "reservado": False}, {"hora": 10, "reservado": False}, 
                                        {"hora": 11, "reservado": False}, {"hora": 12, "reservado": False}, 
                                        {"hora": 13, "reservado": False}]}]},
    
    {"ID": "5", "nombre": "Mariana", "apellido": "Isola", "especialidad": "Nutricionista", 
     "disponibilidad": [
        {"dia": "Viernes", "horarios": [{"hora": 10, "reservado": False}, {"hora": 11, "reservado": False}, 
                                      {"hora": 12, "reservado": False}, {"hora": 13, "reservado": False}]},
        {"dia": "Sabado", "horarios": [{"hora": 10, "reservado": False}, {"hora": 11, "reservado": False}, 
                                          {"hora": 12, "reservado": False}]}]}
]

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


# Inicio Programa
especialidades = imprimirEspecialidades(profesionales)
especialidadSeleccionada = int(input("Ingrese el número de la especialidad que le interesa: ")) - 1
especialidadBuscada = especialidades[especialidadSeleccionada]
imprimirProfesionales(profesionales, especialidadBuscada)
profesionalSeleccionado = int(input("Ingrese el número de la especialidad que le interesa: ")) - 1