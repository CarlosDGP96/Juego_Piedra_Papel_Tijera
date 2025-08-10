import random

print("¡Bienvenido al juego: Piedra, papel o tijera! 😄")

while True:  # Bucle principal para volver a jugar

    pc = random.randint(1, 3)  # Elección aleatoria de la PC

    while True:  # Bucle para validar elección del jugador
        jugador = input("Elige 1 para piedra, 2 para papel, 3 para tijera: ")
        if jugador == '1' or jugador == '2' or jugador == '3':
            jugador = int(jugador)
            break
        else:
            print("¡Error! Debes elegir: 1, 2 o 3")

    if jugador == 1:
        print("Elegiste piedra 🪨")
    elif jugador == 2:
        print("Elegiste papel 📄")
    else:
        print("Elegiste tijera ✂️")

    if pc == 1:
        print("PC elige piedra 🪨")
    elif pc == 2:
        print("PC elige papel 📄")
    else:
        print("PC elige tijera ✂️")

    # Combate Jugador vs PC
    if pc == jugador:
        print("EMPATE")
    elif jugador == 1 and pc == 3:
        print("GANASTE")
    elif jugador == 2 and pc == 1:
        print("GANASTE")
    elif jugador == 3 and pc == 2:
        print("GANASTE")
    else:
        print("PERDISTE")

    respuesta = input("¿Quieres jugar otra vez? (Ingresa la letra S para seguir jugando, o cualquier otra tecla para salir): ")
    if respuesta != 's' and respuesta != 'S':
        print("Gracias por jugar. ¡Hasta luego!")
        break
