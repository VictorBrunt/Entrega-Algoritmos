
def calcular_notas(lista):
    # Media
    media = sum(lista) / len(lista)

    #Nota más alta y más baja
    maxima = max(lista)
    minima = min(lista)

   
    print("Media:", media)
    print("Nota más alta:", maxima)
    print("Nota más baja:", minima)

    #comprobar si hay suspensos
    if minima < 5:
        print("Hay por lo menos una nota suspensa.")
    else:
        print("Todas las notas aprobadas.")


# Ejemplo 
notas = [7, 5, 3, 9, 10]
calcular_notas(notas)
