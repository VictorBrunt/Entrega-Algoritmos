
def analizar_url(url):
    try:
        # Separar protocolo del resto
        partes = url.split("://")
        protocolo = partes[0]

        # Después del protocolo, separar dominio y recurso
        resto = partes[1].split("/", 1)
        dominio = resto[0]

        # Si hay recurso, lo tomo, si no, pongo "ninguno"
        if len(resto) > 1:
            recurso = resto[1]
        else:
            recurso = "ninguno"

        
        print("Protocolo:", protocolo)
        print("Dominio:", dominio)
        print("Recurso:", recurso)

    except:
        print("La URL no es válida.")


# Ejemplo
analizar_url("https://www.ejemplo.com/recurso/pagina1")
