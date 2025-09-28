def clasificar(lista):
    pares = []
    impares = []
    negativos = []

   
    for n in lista:
        # Si es par
        if n % 2 == 0:
            pares.append(n)
        else:  # Si no es par, es impar
            impares.append(n)

        # Si es negativo
        if n < 0:
            negativos.append(n)

    
    return pares, impares, negativos


# Ejemplo:
numeros = [3, -2, 7, 8, -5, 0, 4]
p, i, neg = clasificar(numeros)

print("Pares:", p)
print("Impares:", i)
print("Negativos:", neg)
