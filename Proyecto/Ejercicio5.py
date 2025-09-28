import random

def generar_adn(n):
    letras = ["A", "T", "C", "G"]
    cadena = ""

    #cadena aleatoria
    for i in range(n):
        cadena += random.choice(letras)

    # Conteo
    conteo = {"A": 0, "T": 0, "C": 0, "G": 0}
    for letra in cadena:
        conteo[letra] += 1

    return cadena, conteo


# Ejemplo
adn, conteo = generar_adn(20)
print("Cadena generada:", adn)
print("Conteo:", conteo)
