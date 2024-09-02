import csv

def matriz_a_csv(matriz, nombre_archivo):
    """
    Convierte una matriz en un archivo CSV.

    Args:
    matriz (list of lists): La matriz a convertir en CSV.
    nombre_archivo (str): El nombre del archivo CSV de salida.

    Returns:
    None
    """
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(matriz)

def csv_a_matriz(nombre_archivo):
    matriz = []
    reader = csv.DictReader(nombre_archivo)
    print(reader)
    for row in reader:
        print(row)





#ingresar especialidad


#main
# Ejemplo de uso
matriz = [
    ["Nombre", "Apellido", "Especialidad", "Dia", "Horario de Entrada", "Horario de salida"],
    ["Carlos", "Maslaton", "Oftalmologo", "Martes", 13, 18],
    ["Carlos", "Maslaton", "Oftalmologo", "Miercoles", 13,18],
    ["Carlos", "Maslaton", "Oftalmologo", "Jueves", 13, 18],
    ["Carlos", "Maslaton", "Oftalmologo", "Viernes", 13,18],
    ["Juana", "Gomez", "Otorrina", "Lunes", 10,14],
    ["Juana", "Gomez", "Otorrina", "Martes", 14,19],
    ["Juana", "Gomez", "Otorrina", "Jueves", 9,14],
    ["Martina", "Quintana", "Nutricionista", "Lunes", 10,14]
]

matriz_a_csv(matriz, "salida.csv")
csv_a_matriz("""Nombre,Apellido,Especialidad,Dia,Horario de Entrada,Horario de salida
Carlos,Maslaton,Oftalmologo,Martes,13,18
Carlos,Maslaton,Oftalmologo,Miercoles,13,18
Carlos,Maslaton,Oftalmologo,Jueves,13,18
Carlos,Maslaton,Oftalmologo,Viernes,13,18
Juana,Gomez,Otorrina,Lunes,10,14
Juana,Gomez,Otorrina,Martes,14,19
Juana,Gomez,Otorrina,Jueves,9,14/n
Martina,Quintana,Nutricionista,Lunes,10,14
""")