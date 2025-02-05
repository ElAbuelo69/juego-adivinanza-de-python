import random

numero_secreto = random.randint(0,100)
Adivinado = False

print("Bienvenido al juego de adivinar")

while not Adivinado:
    entrada = input("introduce un número del 1 al 99: ")
    numero = int(entrada)
       
    if numero == numero_secreto:
        print("adivinaste el numero secreto")
        Adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else:
         print("el numero es menor al ingresado")