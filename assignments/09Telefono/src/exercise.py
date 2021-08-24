def main():
    #escribe tu código abajo de esta línea
    #Leer los datos

    costo = float(0.80)

    mensj = int(input("Dame el número de mensajes:"))
    megas = float(input("Dame el número de megas:"))
    min = int(input("Dame el número de minutos:"))

    mens = mensj * costo + megas * costo + min * costo

    print("El costo mensual es:", mens)

pass


if __name__ == '__main__':
    main()
