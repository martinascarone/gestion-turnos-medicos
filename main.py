from archivos import *
from turnos import *
import json

def main():
    ARCHIVO_PROFESIONALES = "db/profesionales.json"
    profesionales = abrirArchivo(ARCHIVO_PROFESIONALES, "rt")
    profesionales = json.load(profesionales)

    verificarExistenciaArchivoTurnos()
    verificarExistenciaArchivoPacientes()

    def inicio():
        print("                ⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                               ⠀")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠸⣷⣦⣀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣦⠀⠠⠾⠿⣿⣷⠀⠀⠀⠀⠀⣠⣤⣄⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⢉⣠⣤⣶⡆⠀⣠⣈⠀⢀⣠⣴⣿⣿⠋⠀⠀⠀⠀                          ")
        print("                     ⠀⢀⡀⢀⣀⣀⣠⣤⡄⢀⣀⡘⣿⣿⣿⣷⣼⣿⣿⣷⡄⠹⣿⡿⠁⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠻⠿⢿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣁⠀⠋⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠈⠻⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣄⣀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⣴⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⠀⣾⣿⣿⣿⣿⣶⡄⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⢀⣾⣿⣷⡀⠻⣿⣿⡿⠻⣿⣿⣿⣿⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⣠⣾⡿⠟⠉⠉⠀⢀⡉⠁⠀⠛⠛⢉⣠⣴⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⢸⣿⣿⡿⠉⠀⠙⠿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠁⠀⠀⠀⠀⠀⠙⠿⣷⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀                          ")
        print("                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                          ")
        print("   ____   _   _           _                        _          _                   _ ")
        print("  / ___| | | (_)  _ __   (_)   ___    __ _      __| |   ___  | |    ___    ___   | |")
        print(" | |     | | | | | '_ \  | |  / __|  / _` |    / _` |  / _ \ | |   / __|  / _ \  | |")
        print(" | |___  | | | | | | | | | | | (__  | (_| |   | (_| | |  __/ | |   \__ \ | (_) | | |")
        print("  \____| |_| |_| |_| |_| |_|  \___|  \__,_|    \__,_|  \___| |_|   |___/  \___/  |_|")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                ⠀")
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
                    visualizarTurnos(profesionales,False)
                case 2:
                    reprogramarTurno(profesionales)
                case 3:
                    reservarTurnos(profesionales)
                case 4:
                    eliminarTurno(profesionales)
                case _:
                    print("Selección inválida. Porfavor, seleccione un número válido.")
main()