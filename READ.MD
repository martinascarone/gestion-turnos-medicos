# Sistema de Gestión de Turnos Médicos

Este proyecto implementa un sistema básico de gestión de turnos médicos, donde los pacientes pueden seleccionar una especialidad médica, elegir un profesional disponible y reservar un turno en un horario determinado.

## Descripción General

El sistema permite:

1. **Visualizar especialidades disponibles.**
2. **Seleccionar profesionales según la especialidad.**
3. **Consultar horarios disponibles para los profesionales.**
4. **Reservar un turno para el paciente en el horario deseado.**

La información de los profesionales, sus horarios y los turnos ya reservados se gestiona mediante listas de diccionarios.

## Estructura de Datos

- `profesionales`: Contiene la lista de profesionales médicos junto con su nombre, apellido y especialidad.
- `disponibilidades`: Lista de los días y horarios en los que cada profesional está disponible.
- `turnos`: Lista de turnos reservados por pacientes, que incluye el paciente, el médico, el día y la hora.
- `pacientes`: Información básica de los pacientes (nombre, apellido y DNI).

## Funcionalidades

### 1. Ver Especialidades
La función `imprimirEspecialidades(lista)` muestra todas las especialidades disponibles en el sistema, permitiendo al usuario seleccionar la especialidad deseada.

### 2. Seleccionar Profesional
Una vez seleccionada la especialidad, la función `imprimirProfesionales(lista, especialidadBuscada)` muestra los profesionales asociados a esa especialidad.

### 3. Ver Horarios Disponibles
La función `imprimirTurnosDisponibles(profesional)` muestra los horarios disponibles del profesional elegido. Los turnos ya ocupados se indican como "OCUPADO", mientras que los disponibles están listados para su selección.

### 4. Reservar Turno
Una vez seleccionado un horario, el turno es registrado mediante la función `seleccionarTurno(idTurno, dia, hora, paciente)`. El sistema también permite ingresar los datos del paciente con la función `solicitarDatos()`.

### 5. Control de Turnos Ocupados
La función `isTurnoOcupado(dia, hora, idMedico)` comprueba si un turno ya ha sido reservado para evitar duplicados.

## Ejecución

Al ejecutar el programa, el flujo general es el siguiente:

1. Se muestra la lista de especialidades disponibles.
2. El usuario selecciona una especialidad.
3. Se muestra la lista de profesionales asociados a esa especialidad.
4. El usuario selecciona un profesional.
5. Se muestran los horarios disponibles del profesional seleccionado.
6. El usuario elige un turno y se registra la reserva.

## Mejoras Futuras

- **Mejorar la función de comprobación de turnos ocupados.**
- **Agregar validación de datos ingresados por el usuario.**
- **Incorporar una interfaz gráfica para facilitar la interacción.**

## Cómo Ejecutar el Proyecto

1. Clonar el repositorio o copiar el código fuente.
2. Asegúrese de tener Python instalado.
3. Ejecutar el script desde la terminal:
   ```bash
   python nombre_del_script.py
