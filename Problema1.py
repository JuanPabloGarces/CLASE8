def sumar_5_enteros():
    # definicion de variables
    lista = []
    contadorWhile = 0
    tamaño = 5
    suma = 0

    # Ingresamos los numeros:
    while contadorWhile < tamaño:
        lista.append(int(input("Ingrese número " + str(contadorWhile) + ": ")))
        contadorWhile += 1

    # sumamos los numeros
    contadorWhile = 0
    while contadorWhile < tamaño:
        suma += lista[contadorWhile]
        contadorWhile

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero, end=', ')

    print("\nla suma de todos los elementos es:")
    print(suma)
