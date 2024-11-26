
def solicitarDatos():
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
    
    with open("db/pacientes.csv", 'a', encoding='utf-8') as archivo:
        archivo.write(f"{dni},{nombre},{apellido}\n")
    
    return dni


def solicitarDNI():
    dni = input("Ingrese su DNI: ")
    
    while not dni.isdigit() or not len(dni)>=6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")
    return dni
    
