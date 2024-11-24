from archivos import leer_pacientes

def solicitarDatos():
    pacientes = leer_pacientes()
    #solicita los datos del paciente y valida entradas
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        print("El nombre debe contener solo letras.")
        nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")
    while not apellido.isalpha():
        print("El apellido debe contener solo letras.")
        apellido = input("Ingrese su apellido: ")

    dni = input("Ingrese su DNI: ")
    while not dni.isdigit() or not len(dni)>=6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")

    id = len(pacientes) + 1
    
    with open("csv/pacientes.csv", 'a', encoding='utf-8') as archivo:
        archivo.write(f"{id},{nombre},{apellido},{dni}\n")
    
    return id


def solicitarDNI():
    dni = input("Ingrese su DNI: ")
    
    while not dni.isdigit() or not len(dni)>=6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")
    return dni
    
