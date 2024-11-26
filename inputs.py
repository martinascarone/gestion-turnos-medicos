
def solicitarDatos():
    # Solicita los datos del paciente y valida entradas
    
    dni = input("Ingrese su DNI: ")
    while not dni.isdigit() or not len(dni) >= 6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")
    
    # Verificar existencia
    # si existe mensaje de bienvenida
    pacientes = open("db/pacientes.csv", "rt")
    linea = pacientes.readline()
    while linea != "": 
        valores = linea.strip().split(',')
        if valores[0] == dni:
            existe = True
            break
        else:
            existe = False
            linea = pacientes.readline()

    if existe:
        print(f"\n\nBienvenido {valores[1]} {valores[2]}")
    else:
        nombre = input("Ingrese su nombre: ")
        while not nombre.isalpha():
            print("El nombre debe contener solo letras.")
            nombre = input("Ingrese su nombre: ")

        apellido = input("Ingrese su apellido: ")
        while not apellido.isalpha():
            print("El apellido debe contener solo letras.")
            apellido = input("Ingrese su apellido: ")

        print(f"\n\nBienvenido {nombre} {apellido}")
        archivo = open("db/pacientes.csv", "at")
        archivo.write(f"{dni},{nombre},{apellido}\n")
        archivo.close()    


    return dni

def solicitarDNI():
    dni = input("Ingrese su DNI: ")
    
    while not dni.isdigit() or not len(dni)>=6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")
    return dni
    
