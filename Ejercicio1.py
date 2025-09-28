
mensaje = input("Pega el mensaje cifrado: ")

#Vuelta al mensaje
invertido = mensaje[::-1]

#Quitar lo que no sean letras
limpio = ""
for ch in invertido:
    if ch.isalpha():   # si es una letra, la añado
        limpio = limpio + ch

print("Mensaje limpio:", limpio)
