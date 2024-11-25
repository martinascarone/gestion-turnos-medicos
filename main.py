from archivos import *
from turnos import *

def main():
    ARCHIVO_PACIENTE = "/db/pacientes.csv"
    ARCHIVO_PROFESIONALES = "db/profesionales.json"
    profesionales = abrirArchivo(ARCHIVO_PROFESIONALES, "rt")
    profesionales = json.load(profesionales)
    print(profesionales)
    def inicio():
        print("\n--- Clinica del Sol ---")
        print("\n1) Ver mis turnos")
        print("2) Reprogramar un turno")
        print("3) Reservar un turno")
        print("4) Cancelar turno")
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
            
            match opcion_selec:
                case -1:
                    print("Saliendo...")
                    break
        
                case 1:
                    visualizarTurnos()
                case 2:
                    modificarTurnos()
                case 3:
                    reservarTurnos(profesionales)
                case 4:
                    eliminarTurno()
                case _:
                    print("Selección inválida. Porfavor, seleccione un número válido.")
main()