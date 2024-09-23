import random


def generarListaEspecialidades(matriz):
    '''
    se ingresa la matirz con los datos de los profesionales, sale listado de especialidades sin duplicados
    '''
    listaEspecialidades = []
    for i in range(1, len(matriz)):
        especialidad = matriz[i][3]
        if especialidad not in listaEspecialidades:
            listaEspecialidades.append(especialidad)
    print(f"{listaEspecialidades}")
    return listaEspecialidades


def imprimirEspecialidades(especialidades):
    print(f"llegaron: {especialidades}")
    indice = 0
    print("Hola! ¿Qué especialidad estás buscando?")
    while indice < len(especialidades):
        print(indice + 1, ")", especialidades[indice])
        indice += 1
    print("-1) Finalizar")


def ingresarEspecialidad(especialidades):
    seleccion = (int(input("Ingrese el número de especialidad: "))) - 1
    if seleccion == -2:
        print("Finalizando...")
        return None
    if seleccion >= 0 and seleccion < len(especialidades):
        return especialidades[seleccion]
    else:
        print("Opción inválida")
        return ingresarEspecialidad(especialidades)


def mostrarProfesionales(matriz, especialidadSeleccionada, horarios):
    """
    mostrar profesionales disponibles de la espeialidad seleccionada
    """
    # Filtramos los profesionales que coincidan con la especialidad seleccionada
    print(f"Especialidad seleccionada: {especialidadSeleccionada}")
    profesionales = []
    for i in range(1, len(matriz)):
        if matriz[i][3] == especialidadSeleccionada:
            profesionales.append(matriz[i][1] + " " + matriz[i][2])
    indice = 0
    print("Profesionales disponibles de la especialidad seleccionada:")
    while indice < len(profesionales):
        print(indice + 1, ")", profesionales[indice])
        indice += 1


def mostrarDisponibilidad(matriz):
    """
    mostrar dias disponibles
    mostrar horarios disponibles
    """


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



#ingresar especialidad

#main
# Ejemplo de uso
matrizProfesionales = [[
    "ID Profesional", "Nombre", "Apellido", "Especialidad"
], ["1", "Carlos", "Maslaton", "Oftalmologo"],
                       ["2", "Juan", "Rodriguez", "Oftalmologo"],
                       ["3", "Juana", "Gomez", "Pediatra"],
                       ["4", "Martina", "Quintana", "Nutricionista"]]
matrizHorarios = [[
    "ID Profesional", "Dia", "Horario de entrada", "Horario de salida"
], ["1", "Lunes", 13, 18], ["1", "Miercoles", 13, 18], ["1", "Jueves", 13, 18],
                  ["2", "Viernes", 13, 18], ["3", "Lunes", 10, 14],
                  ["3", "Martes", 14, 19], ["3", "Jueves", 9, 14],
                  ["4", "Lunes", 10, 14]]
pacienteMatriz = [["id", "nombre", "apellido", "dni"]]

turnosMatriz = [[
    "id", " id paciente", "id medico", "horario", "fecha", "observacion"
]]
"""
ingresar profesional, ingresar paciente, mostrar dias disponibles, mostrar horarios disponibles, seleccionar uno, almacenar en pacientes. 

"""
#Inicio Peograma
"""crear funcion que muestre las fechas disponibles de cada medico!!!!!!!!
decir cual es el trno libre mas proximo"""

#pacienteMatriz = [nombre, apellido, dni, id]

#generarListaEspecialidades(matriz)
#imprimirDatos(matriz)
especialidades = generarListaEspecialidades(matrizProfesionales)
imprimirEspecialidades(especialidades)
especialidad = ingresarEspecialidad(especialidades)

if especialidad:
    mostrarProfesionales(matrizProfesionales, especialidad, matrizHorarios)
    profesional = input("Ingrese el número del profesional: ")
    mostrarDisponibilidad(matrizHorarios, profesional)
    solicitardatos(pacienteMatriz)
else:
    print("No se selecciono ninguna especialidad")