
def solicitarDatos():
    # Solicita los datos del paciente y valida entradas
    
    dni = input("Ingrese su DNI: ")
    while not dni.isdigit() or len(dni) < 6:
        print("El DNI debe contener solo números y tener al menos 6 dígitos.")
        dni = input("Ingrese su DNI: ")
    
    try:
        pacientes = open("db/pacientes.csv", "rt")
        linea = pacientes.readline()
        existe = False
        while linea != "":  # Leer línea por línea
            valores = linea.strip().split(',')
            if valores[0] == dni:
                existe = True
                print(f"\n\nBienvenido {valores[1]} {valores[2]}")
                break
            linea = pacientes.readline() 
        pacientes.close() 

        if not existe:
            nombre = input("Ingrese su nombre: ")
            while not nombre.isalpha():
                print("El nombre debe contener solo letras.")
                nombre = input("Ingrese su nombre: ")

            apellido = input("Ingrese su apellido: ")
            while not apellido.isalpha():
                print("El apellido debe contener solo letras.")
                apellido = input("Ingrese su apellido: ")

            archivo = open("db/pacientes.csv", "at")
            archivo.write(f"{dni},{nombre},{apellido}\n")
            archivo.close() 
            
            print(f"\n\nBienvenido {nombre} {apellido}")
        
        return dni

    except FileNotFoundError:
        try:
            archivo = open("db/pacientes.csv", "wt")
            archivo.close()
            # Se llama a si misma para volver al flujo normal
            return solicitarDatos()
        
        except Exception :
            print(f"Error al crear el archivo")
            return None

def solicitarDNI():
    dni = input("Ingrese su DNI: ")
    
    while not dni.isdigit() or not len(dni)>=6:
        print("El DNI debe contener solo números.")
        dni = input("Ingrese su DNI: ")
    return dni
    
