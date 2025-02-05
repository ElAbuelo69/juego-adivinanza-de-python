
while True:
    jugador1 = input("Que elige jugador 1, piedra, papel o tijera: ").lower()
    jugador2 = input("Que elige jugador 2, piedra, papel o tijera: ").lower()

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Ganó jugador 1")
    else:
        print("Ganó jugador 2")

    repetir = input("¿Quieres volver a jugar? (si/no): ").lower()
    if repetir != "si":
        print("Gracias por jugar!")
        break