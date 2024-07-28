import random
from random import choice
import os
def borrar_pantalla():  #   función reutilizable para borrar la pantalla
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def bienvenida():
    borrar_pantalla()
    print("Hola, bienvenido!!\n\nEstas listo para jugar Piedra Papel o Tijera??\n\nAl mejor de tres intentos?\n")
    jugar= input("Ingresa enter para jugar o SALIR para salir").lower()
    borrar_pantalla()
    if jugar != "":
        exit()

def nombre_jugador():
    global nombre
    nombre = input("¡Hola jugador! por favor Ingresa tu nombre!\n ").capitalize()
    return nombre

def obtener_opciones():
    return [
        {"opcion": 1, "nombre": "Piedra"},
        {"opcion": 2, "nombre": "Papel"},
        {"opcion": 3, "nombre": "Tijera"},
    ]

def obtener_seleccion_usuario():
    borrar_pantalla()
    while True:
        try:
            seleccion = int(input("""-----------------------------------------------------------------\n
  """ + nombre + """ elije un número: (1) Piedra, (2) Papel o (3) Tijera:\n
-----------------------------------------------------------------\n"""))
            if seleccion in [1, 2, 3]:
                return seleccion               
        except ValueError:
            print("Opción no válida, por favor elige 1, 2 o 3.\nEntrada no válida, por favor introduce un número.")
            input(nombre + " Presiona una tecla para continuar")
            borrar_pantalla()

def determinar_ganador(user_selection, cpu_selection):
    if user_selection == cpu_selection:
        return "empate"
    if (user_selection == 1 and cpu_selection == 3) or \
       (user_selection == 2 and cpu_selection == 1) or \
       (user_selection == 3 and cpu_selection == 2):
        return "usuario"
    return "cpu"

def jugar_ronda(options):
    cpu_selected = choice(options)
    user_selected = obtener_seleccion_usuario()

    ganador = determinar_ganador(user_selected, cpu_selected["opcion"])
    
    if ganador == "empate":
        print(f"La computadora también eligió {cpu_selected['nombre']}, vamos de nuevo!")
    elif ganador == "usuario":
        print(f"La computadora había elegido: {cpu_selected['nombre']}. " + nombre + " ganaste esta ronda!")
    else:
        print(f"La computadora había elegido: {cpu_selected['nombre']}.\nLa computadora gana esta ronda")
    input("----------------------------------------------------\nPresiona una tecla para continuar")
    borrar_pantalla()
    return ganador

def jugar_juego():
    borrar_pantalla()
    options = obtener_opciones()
    user_wins = 0
    cpu_wins = 0
    while user_wins < 2 and cpu_wins < 2:
        ganador = jugar_ronda(options)
        if ganador == "usuario":
            user_wins += 1
        elif ganador == "cpu":
            cpu_wins += 1

    if user_wins == 2:
        print(nombre + " ganaste el juego al mejor de 3!")
        return "user"
    else:
        print("La computadora ganó el juego al mejor de 3!")
        return "cpu"

def main():
    bienvenida()
    nombre_jugador()
    list_of_winners = []
    play_again = True

    while play_again:
        ganador = jugar_juego()
        list_of_winners.append(ganador)
        play_again = input(nombre + "\n¿Deseas jugar de nuevo?\n(Presiona s para jugar cualquier tecla para salir)\n").lower() == "s"
        borrar_pantalla()

    print("--------\n" + nombre + "\nGracias por jugar! A continuación se muestra el historial de ganadores:")
    print(list_of_winners)

if __name__ == "__main__":
    main()
