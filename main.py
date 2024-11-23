def main():
    def leer_disponibilidades():
        ruta_archivo = "csv/disponibilidad.csv"
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo: #asignamos el archivo abierto a la variable archivo
            lineas = archivo.readlines()
            
        encabezados = lineas[0].strip().split(',') # seleccionamos la primera linea de la lista (encabezados), split dividie la lista usando, como separador
        datos = []
        
        for linea in lineas[1:]: # usamos slicing para obtener un subconjunto de lineas iniciando desde el i 1
            valores = linea.strip().split(',')
            registro = {encabezados[i]: valores[i] for i in range (len(encabezados))}
            datos.append(registro)
        #print("disponib:", datos)
        return datos  
        
    def leer_profesionales():
        ruta_archivo = "csv/profesionales.csv"
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo: 
            lineas = archivo.readlines()
        
        encabezadosProf = lineas[0].strip().split(',') 
        datosProf = []
        
        for linea in lineas[1:]: 
            valores = linea.strip().split(',')
            registro = {encabezadosProf[i]: valores[i] for i in range (len(encabezadosProf))}
            datosProf.append(registro)
        #print("prof:", datosProf)
        return datosProf  
    
    def leer_pacientes():
        ruta_archivo = "csv/pacientes.csv"
        try: #colocamos un try catch por si el archivo esta vacio
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo: 
                lineas = archivo.readlines()
            # Verificar si el archivo está vacío
            if not lineas:
                print("no hay registros almacenados")
                return []

            encabpacientes = lineas[0].strip().split(',') 
            pacientes = []

            for linea in lineas[1:]: 
                valores = linea.strip().split(',')
                registro = {encabpacientes[i]: valores[i] for i in range (len(encabpacientes))}
                pacientes.append(registro)
            print(pacientes)
            return pacientes
        except FileNotFoundError:
            print(f"Error: El archivo {ruta_archivo} no se encontró.")
            return []
        except IndexError as e:
            print(f"Error de índice al procesar el archivo: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado: {e}")
            return []
    
    
    
    disponibilidades = leer_disponibilidades()
    profesionales = leer_profesionales()
    #pacientes = leer_pacientes() aca no se llama

    turnos = []
    
    #def eliminarTurno():
    
    def solicitarDNI():
        dni = input("Ingrese su DNI: ")
        
        while not dni.isdigit() or not len(dni)>=6:
            print("El DNI debe contener solo números.")
            dni = input("Ingrese su DNI: ")
        return dni
    
    def modificarTurnos():
        dni = visualizarTurnos()
        #ingrese que turno le gustaria modificar
        #elimna el turno
        #aca lo mandaria al seleccione especialidad para que se agende el nuevo numero        
     
        
        
    def visualizarTurnos():
        dni = solicitarDNI()
        ruta_archivo = "csv/turnos.csv"
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split(',')
                
                if not encabezados or encabezados == ['']:
                    print("Archivo vacio")
                    return

                turnos_encontrados = False
                contador = 1
                
                for linea in archivo:
                    valores = linea.strip().split(',')
                    registro = {encabezados[i]: valores[i] for i in range(len(encabezados))} #diccionario con el registro
                    
                    if dni in valores:
                        dia = registro["dia"] if "dia" in registro else "no hay dia"
                        hora = registro["hora"] if "hora" in registro else "no hay hora"
                        print(f"{contador}) Tiene turno agendado para el dia {dia} a las {hora} hs.")
                        
                        turnos_encontrados = True
                        contador += 1
                if turnos_encontrados:
                    return dni  # Retorna el dni después de procesar todos los turnos
                else:
                    print("No tiene turnos asociados")
                    print("Volviendo al menu principal...")

        except FileNotFoundError:
            print("Error el archivo no se encontro")
        except Exception as e:
            print(f"Error inesperado: {e}")
            
    
    def reservarTurnos():
        especialidadSeleccionada = 0 
        while True:
            especialidades = imprimirEspecialidades(profesionales)

            while True:
                try:
                    especialidadSeleccionada = int(input("Ingrese el número de la especialidad que le interesa (o -1 para salir): ")) - 1

                    if especialidadSeleccionada == -2:  # arreglamos indice
                        print("Finalizó Reserva.")
                        return

                    if especialidadSeleccionada < -1 or especialidadSeleccionada >= len(especialidades):
                        print("Selección inválida. Por favor, seleccione un número válido.")
                        continue
                    break  

                except ValueError:
                    print("Error: Debe ingresar un número válido.")

            if especialidadSeleccionada == -2:  # arreglamos indice
                break
            
            #obtenemos la especialidad
            especialidadBuscada = especialidades[especialidadSeleccionada]
            imprimirProfesionales(profesionales, especialidadBuscada)

            #seleccionamos el profesional
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
        pass
    
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
                contadorHoras = int(turno["horarioSalida"]) - int(turno["horarioEntrada"])
                for hora in range(contadorHoras):
                    dia = turno["dia"]
                    hora_actual = int(turno["horarioEntrada"]) + hora
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

    def inicio():
        print("\n--- Clinica del Sol ---")
        
        print("\n1) Ver mis turnos")
        print("2) Modificar un turno")
        print("3) Reservar un turno")
        print("-1) Salir")
        try:
            opcion = int(input(("\nIngrese un número para continuar: ")))
            return opcion
        except ValueError:
                print("Error: Debe ingresar un numero valido: ")

    def solicitarDatos(pacientes):
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



    # Inicio Programa
    opcion_selec = 0
    
    while True:
            opcion_selec = inicio()
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
                reservarTurnos()
            else:
                print("Selección inválida. Porfavor, seleccione un número válido.")
            
main()


'''
1.mejor  interfaz (ver mis turnos)
2.modificar turnos 
3.eliminar turnos
4. try/catch

'''
