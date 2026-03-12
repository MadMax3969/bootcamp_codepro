palabra_a_encontrar = "circo"
intentos = 5
cantidad_letras_de_palabra_a_encontrar = len(palabra_a_encontrar)


def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    letras_verificadas = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar):

        if palabra_a_encontrar[posicion] == palabra_ingresada[posicion]:
            letras_verificadas.append("[" + palabra_ingresada[posicion] + "]")

        elif palabra_ingresada[posicion] in palabra_a_encontrar:
            letras_verificadas.append("(" + palabra_ingresada[posicion] + ")")

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas


if intentos > 0:
    print(f"Te quedan {intentos} intentos")
    intentos -= 1
    palabra_ingresada = input("Ingrese su palabra: ")

    while True:
        if len(palabra_ingresada) != cantidad_letras_de_palabra_a_encontrar:
            print(f'La palabra debe tener {cantidad_letras_de_palabra_a_encontrar} cantidad de palabras')
            break
        else:
            print(list(palabra_ingresada))
        if palabra_ingresada == palabra_a_encontrar:
            print("Ganaste")
            break
        
else:
    print(f"Perdiste la palabra era: {palabra_a_encontrar}")