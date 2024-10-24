def main():
    profesionales = [
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
            "idMedico": "1",
            "dia": "Lunes",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "1",
            "dia": "Miércoles",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "1",
            "dia": "Jueves",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "2",
            "dia": "Martes",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "2",
            "dia": "Viernes",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "2",
            "dia": "Sábado",
            "horarioEntrada": 13,
            "horarioSalida": 17,
        },
        {
            "idMedico": "3",
            "dia": "Lunes",
            "horarioEntrada": 10,
            "horarioSalida": 13,
        },
        {
            "idMedico": "3",
            "dia": "Martes",
            "horarioEntrada": 14,
            "horarioSalida": 18,
        },
        {
            "idMedico": "4",
            "dia": "Jueves",
            "horarioEntrada": 9,
            "horarioSalida": 13,
        },
        {
            "idMedico": "4",
            "dia": "Lunes",
            "horarioEntrada": 10,
            "horarioSalida": 13,
        },
        {
            "idMedico": "4",
            "dia": "Miércoles",
            "horarioEntrada": 10,
            "horarioSalida": 12,
        },
        {
            "idMedico": "5",
            "dia": "Martes",
            "horarioEntrada": 9,
            "horarioSalida": 12,
        },
        {
            "idMedico": "5",
            "dia": "Jueves",
            "horarioEntrada": 14,
            "horarioSalida": 17,
        },
        {
            "idMedico": "6",
            "dia": "Viernes",
            "horarioEntrada": 9,
            "horarioSalida": 13,
        },
        {
            "idMedico": "7",
            "dia": "Viernes",
            "horarioEntrada": 10,
            "horarioSalida": 13,
        }
    ]

    turnos = []

    pacientes = []
    
    #def modificarTurno():
    
    #def eliminarTurno():
    
    #def visualizarTurnos():
    

    def isTurnoOcupado(dia, hora, idMedico):
        for turno in turnos:
            if turno["dia"] == dia and turno["hora"] == hora and int(turno["idMedico"]) == int(idMedico):
                return True
        return False

    def imprimirTurnosDisponibles(profesional):
        contador = 0
        opciones = []

        print("┌" + ("─"*4) + "┬" + ("─"*12) + "┬" + ("─"*10) + "┬" + ("─"*15) + "┐")
        print("│" + " " + "   " + "│" + " " + "Día" + " " * 8 + "│" + " " + "Horario" + "  " + "│" + " " + "Disponibilidad" +"│")
        print("├" + "─"*4 + "┼" + "─"*12 + "┼" + "─"*10 + "┼" + "─"*15 + "┤")

        for turno in disponibilidades:
            if turno["idMedico"] == str(profesional):
                contadorHoras = turno["horarioSalida"] - turno["horarioEntrada"]
                for hora in range(contadorHoras):
                    dia = turno["dia"]
                    hora_actual = turno["horarioEntrada"] + hora
                    ocupado = isTurnoOcupado(dia, hora_actual, profesional)
                    opciones.append({
                        "dia": dia,
                        "hora": hora_actual,
                        "ocupado": ocupado
                    })

                    disponibilidad_texto = "OCUPADO" if ocupado else "DISPONIBLE"
                    print(f"│ {contador + 1:<3}│ {dia:<10} │ {hora_actual:<8} │ {disponibilidad_texto:<13} │")
                    contador += 1

        print("└" + "─"*4 + "┴" + "─"*12 + "┴" + "─"*10 + "┴" + "─"*15 + "┘")

        while True:
            turnoSeleccionado = input("Ingrese el número del turno que desea seleccionar: ")
            if turnoSeleccionado.isdigit():
                turnoSeleccionado = int(turnoSeleccionado) - 1
                if turnoSeleccionado < 0 or turnoSeleccionado >= len(opciones):
                    print("Selección inválida. Por favor, seleccione un número válido.")
                    continue
                if opciones[turnoSeleccionado]["ocupado"]:
                    print("El turno seleccionado está ocupado. Por favor, seleccione otro turno.")
                else:
                    return opciones[turnoSeleccionado]["dia"], opciones[turnoSeleccionado]["hora"]
            else:
                print("Debe ingresar un número válido.")
        contador = 0
        opciones = []
        for turno in disponibilidades:
            if turno["idMedico"] == str(profesional):
                contadorHoras = turno["horarioSalida"] - turno["horarioEntrada"]
                for hora in range(contadorHoras):
                    dia = turno["dia"]
                    hora_actual = turno["horarioEntrada"] + hora
                    ocupado = isTurnoOcupado(dia, hora_actual, profesional)
                    opciones.append({
                        "dia": dia,
                        "hora": hora_actual,
                        "ocupado": ocupado
                    })
                    if ocupado:
                        print("┌────────────────────────────────────────────────┐\n" + "│")
                        print(contador + 1, ")", dia, hora_actual, "hs OCUPADO")
                    else:
                        print(contador + 1, ")", dia, hora_actual, "hs")
                    contador += 1
        while True:
            turnoSeleccionado = input("Ingrese el número del turno que desea seleccionar: ")
            if turnoSeleccionado.isdigit():
                turnoSeleccionado = int(turnoSeleccionado) - 1
                if turnoSeleccionado < 0 or turnoSeleccionado >= len(opciones):
                    print("Selección inválida. Por favor, seleccione un número válido.")
                    continue
                if opciones[turnoSeleccionado]["ocupado"]:
                    print("El turno seleccionado está ocupado. Por favor, seleccione otro turno.")
                else:
                    return opciones[turnoSeleccionado]["dia"], opciones[turnoSeleccionado]["hora"]
            else:
                print("Debe ingresar un número válido.")


    def seleccionarTurno(idTurno, dia, hora, paciente):
        turnos.append(
            {
                "id": str(len(turnos) + 1),
                "idPaciente": int(paciente),
                "idMedico": int(idTurno),
                "dia": dia,
                "hora": hora
            })
        print("\n-------------------------------------------------" )
        print(f"Turno reservado para el día {dia} a las {hora}:00 hs")
        print("-------------------------------------------------\n" )



    def generarListaEspecialidades(lista):
    #ingresa lista de diccionarios con datos de profesionales, sale listado de especialidades sin duplicados
    #genera lista de especialidades sin duplicados    
        listaEspecialidades = []
        for profesional in lista:
            especialidad = profesional["especialidad"]
            if especialidad not in listaEspecialidades:
                listaEspecialidades.append(especialidad)
        return listaEspecialidades


    def imprimirEspecialidades(lista):
    #imprime toda las especialidades disponibles
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

    #funcion lambda para generar lista de profesionales asosciados a la especialidad seleccionada
    generarListaProfesionales = lambda lista, especialidadBuscada: list(filter(lambda p: p["especialidad"] == especialidadBuscada, lista))

    def imprimirProfesionales(lista, especialidadBuscada):
    #mostrar todos los profesionales de la especialidad
        profesionales = generarListaProfesionales(lista, especialidadBuscada)
        indice = 0
        while indice < len(profesionales):
            print(indice + 1, ")", profesionales[indice]["nombre"], profesionales[indice]["apellido"])
            indice += 1



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

        id = len(pacientes) + 1
        pacientes.append([id, nombre, apellido, dni])
        return id



    # Inicio Programa
    especialidadSeleccionada = 0 

    while especialidadSeleccionada != -1:
        especialidades = imprimirEspecialidades(profesionales)

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
        imprimirProfesionales(profesionales, especialidadBuscada)


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

        seleccionarTurno(
            profesionalSeleccionado + 1,
            dia,
            hora,
            solicitarDatos()
        )
main()


'''
1.mejor  interfaz (ver mis turnos)
2.modificar turnos 
3.eliminar turnos
4. try/catch

'''
