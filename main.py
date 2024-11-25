from archivos import *
from turnos import *

def main():
    ARCHIVO_PACIENTE = "/db/pacientes.csv"
    ARCHIVO_PROFESIONALES = "db/profesionales.json"

    pacientes = []
    profesionales = abrirArchivo(ARCHIVO_PROFESIONALES, "rt")
    profesionales = json.load(profesionales)
    print(profesionales)
    def inicio():
        print("\n--- Clinica del Sol ---")
        print("\n1) Ver mis turnos")
        print("2) Reprogramar un turno")
        print("3) Reservar un turno")
        print("-1) Salir")
        try:
            opcion = int(input(("\nIngrese un número para continuar: ")))
            return opcion
        except ValueError:
                print("Error: Debe ingresar un numero valido: ")


    # Inicio Programa
    opcion_selec = 0
    
    while True:
            opcion_selec = inicio()
            # TODO: Reemplazar estas condiciones por un Switch case
            # y agregar la opcion de cancelar turno
            # Responsable: Martina Scarone
            if opcion_selec is None:
                continue
            
            if opcion_selec == -1:
                print("Saliendo...")
                break
        
            if opcion_selec == 1:
                visualizarTurnos()
            elif opcion_selec == 2:
                modificarTurnos()
            elif opcion_selec == 3:
                reservarTurnos(profesionales)
            else:
                print("Selección inválida. Porfavor, seleccione un número válido.")

'''
pacientes_archivo.write(nombre + ',' + apellido + ',' + dni + '\n')
        pacientes_archivo.close()
        return dni

    # Inicio Programa
    especialidadSeleccionada = 0 

    while especialidadSeleccionada != -1:
        especialidades = imprimirEspecialidades(cargarProfesionales())

        while True:
            try:
                especialidadSeleccionada = int(input("Ingrese el número de la especialidad que le interesa (o -1 para salir): ")) - 1

                if especialidadSeleccionada == -2:  # arreglamos indice
                    print("Finalizó Reserva.")
                    break

                if especialidadSeleccionada < -1 or especialidadSeleccionada >= len(especialidades):
                    print("Selección inválida. Por favor, seleccione un número válido.")
                    continue
                break  

            except ValueError:
                print("Error: Debe ingresar un número válido.")

        if especialidadSeleccionada == -2:  # arreglamos indice
            break

        especialidadBuscada = especialidades[especialidadSeleccionada]
        imprimirProfesionales(cargarProfesionales(), especialidadBuscada)


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
        print(dia, hora)
    guardarImprimirTurno(
            profesionalSeleccionado + 1,
            dia,
            hora,
            solicitarDatos()
        )
'''       
main()