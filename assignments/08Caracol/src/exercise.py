def main():
    #escribe tu código abajo de esta línea

    vel = float(5.7)
    min = float(input("Dame los minutos:"))

    dis = (vel * (min*60))/10

    print("Centímentros recorridos:", dis)
    
pass

if __name__ == '__main__':
    main()
