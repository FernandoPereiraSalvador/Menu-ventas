# Fernando José Pereira Salvador

# Inicializamos los vectores y variables
opcion = 0
nombres = []
precios = []
cantidad_vendida = []
articulo_seleccionado = ""
posicion_articulo_seleccionado = int()
salir = "n"

# Se imprime el menu siempre que la opcion sea verdadera
while salir == "n":

    print("1.Introduce un nuevo articulo")
    print("2. Haz una venta")
    print("3. Mostrar información")
    print("4. Borrar un articulo")
    print("5. Borrar todos los articulos")
    print("6. Salir")

    try:
        opcion = int(input("Introduce un numero: "))
    except:
        print("No has introducido un numero valido")

# Introducimos un articulo nuevo
    if opcion == 1:
        try:
            nombres.append(str(input("Introduce el nombre del articulo: ")))
            precios.append(float(input("Introduce el precio del articulo: ")))
            cantidad_vendida.append(0)
        except:
            print("Has introducido un valor no valido")
            nombres.pop()
        print("\n")

# Hacer una venta
    elif opcion == 2:
        try:
            articulo_seleccionado = str(input("Introduce el nombre del articulo vendido: "))
            posicion_articulo_seleccionado = nombres.index(articulo_seleccionado)
            cantidad_vendida[posicion_articulo_seleccionado] += int(input("Introduce la cantidad vendida: "))
        except ValueError:
            print("No se ha encontrado en la lista")
        print("\n")

# Mostrar información
    elif opcion == 3:
        if len(nombres) >= 1:
            articulo_mas_vendido = 0
            articulo_mas_ingresos = 0
            total = 0
            print("%10s %10s %10s %10s" % ("NOMBRE", "CANTIDAD", "PRECIO", "IMPORTE"))
            for i in range(0, len(nombres)):
                importe = cantidad_vendida[i] * precios[i]
                total += importe

                if cantidad_vendida[articulo_mas_vendido] < cantidad_vendida[i]:
                    articulo_mas_vendido = i
                if articulo_mas_ingresos < importe or articulo_mas_ingresos == 0:
                    articulo_mas_ingresos = i

                print("%10s" % nombres[i],end="")
                print("%10d" % cantidad_vendida[i],end="")
                print("%10d" % precios[i],end="")
                print("%10d" % importe, end="")
                print("")
            print("%31s %10d" % ("TOTAL", total))
            print("%20s" % f"Articulo mas vendido: {nombres[articulo_mas_vendido]} con {cantidad_vendida[articulo_mas_vendido]} unidades")
            print("%20s" % f"Articulo con mas ingresos: {nombres[articulo_mas_ingresos]} con {cantidad_vendida[articulo_mas_ingresos] * precios[articulo_mas_ingresos]} euros")
        else:
            print("No has introducido ningun articulo")
        print("\n")

# Eliminar un articulo
    elif opcion == 4:
        try:
            articulo_seleccionado = str(input("Introduce el articulo que quieras eliminar: "))
            posicion_articulo_seleccionado = nombres.index(articulo_seleccionado)

            nombres.pop(posicion_articulo_seleccionado)
            precios.pop(posicion_articulo_seleccionado)
            cantidad_vendida.pop(posicion_articulo_seleccionado)

            print(f"El articulo {articulo_seleccionado} se ha eliminado correctamente\n")
        except ValueError:
            print(f"No se ha encontrado el articulo {articulo_seleccionado}\n")
        print("\n")

# Eliminar todos los articulos
    elif opcion == 5:
        nombres = []
        precios = []
        cantidad_vendida = []
        print("Se han borrado todos los articulos correctamente\n")

# Salir del bucle
    elif opcion == 6:
        salir = input("¿Estas seguro de que quieres salir? (s/n): ")
        print("\n")
    else:
        print("Has introducido una opcion invalida\n")
