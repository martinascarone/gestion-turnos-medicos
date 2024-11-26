
def imprimirProfesionales(lista, especialidadBuscada):
    #funcion lambda para generar lista de profesionales asosciados a la especialidad seleccionada
    generarListaProfesionales = lambda lista, especialidadBuscada: list(filter(lambda p: p["especialidad"] == especialidadBuscada, lista))
    #mostrar todos los profesionales de la especialidad
    profesionales = generarListaProfesionales(lista, especialidadBuscada)
    indice = 0
    while indice < len(profesionales):
        print(indice + 1, ")", profesionales[indice]["nombre"], profesionales[indice]["apellido"])
        indice += 1

    return len(profesionales)


def obtenerIdDeProfesional(lista,especialidadBuscada,indice):
    generarListaProfesionales = lambda lista, especialidadBuscada: list(filter(lambda p: p["especialidad"] == especialidadBuscada, lista))
    profesionales = generarListaProfesionales(lista, especialidadBuscada)
    return profesionales[indice-1]["id"]