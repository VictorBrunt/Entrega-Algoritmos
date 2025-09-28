cantidad_inicial = int(input("Cantidad inicial (€): "))
cantidad_mensual = int(input("Cantidad que ahorras cada mes (€): "))
meses = int(input("Número de meses: "))

#Cálculo del total ahorrado
total = cantidad_inicial + (cantidad_mensual * meses)


print("Al final tendrás:", total, "€")

#si pasa de 5000€, felicitar
if total > 5000:
    print("¡Felicidades, has ahorrado más de 5000€!")
