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
# Imprime toda las especialidades disponibles
    especialidades = generarListaEspecialidades(lista)
    indice = 0
    print("Hola! ¿Qué especialidad estás buscando?")
    while indice < len(especialidades):
        print(indice + 1, ")", especialidades[indice])
        indice += 1
    print("-1) Finalizar")
    return especialidades