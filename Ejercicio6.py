
def inventario(personajes):
    humanos = []
    criaturas = []

    # Separar en listas
    for nombre, tipo in personajes.items():
        if tipo == "humano":
            humanos.append(nombre)
        elif tipo == "criatura":
            criaturas.append(nombre)

    # Ordenar
    humanos.sort()  # alfabéticamente
    criaturas.sort(key=len)  # por longitud del nombre

    return humanos, criaturas


# Ejemplo
personajes = {
    "Aragorn": "humano",
    "Legolas": "humano",
    "Gondor": "humano",
    "Orco": "criatura",
    "Trol": "criatura",
    "Dragón": "criatura"
}

h, c = inventario(personajes)

print("Humanos ordenados:", h)
print("Criaturas ordenadas:", c)
