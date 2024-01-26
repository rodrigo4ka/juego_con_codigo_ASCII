print("                                                                                       ")
print("  ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄ ") 
print(" █    █      ▐ ▄▀ ▀▄ ▐ ▄▀   █ ▐  ▄▀   ▐ █   █   █ █   █  █  █  █ █ █ █    █  ▐ █      █")
print(" ▐    █        █▄▄▄█   █▄▄▄▀    █▄▄▄▄▄  ▐  █▀▀█▀  ▐   █  ▐  ▐  █  ▀█ ▐   █     █      █")
print("     █        ▄▀   █   █   █    █    ▌   ▄▀    █      █       █   █     █      ▀▄    ▄▀")
print("   ▄▀▄▄▄▄▄▄▀ █   ▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▄   █     █    ▄▀▀▀▀▀▄  ▄▀   █    ▄▀         ▀▀▀▀  ") 
print("   █         ▐   ▐   █    ▐    █    ▐   ▐     ▐   █       █ █    ▐   █                 ")
print("   ▐                 ▐         ▐                  ▐       ▐ ▐        ▐                 ")
print("                                                                                                                                                           ")                                                                                           
print(" ▄▀▀█▄▄   ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄      ▄▀▀█▄       ▄▀▀▄ ▄▀▄  ▄▀▀▄  ▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ") 
print(" █ ▄▀   █ ▐  ▄▀   ▐     █    █      ▐ ▄▀ ▀▄     █  █ ▀  █ █   █    █ ▐  ▄▀   ▐ █   █   █ █    █  ▐ ▐  ▄▀   ▐ ")
print(" ▐ █    █   █▄▄▄▄▄      ▐    █        █▄▄▄█     ▐  █    █ ▐  █    █    █▄▄▄▄▄  ▐  █▀▀█▀  ▐   █       █▄▄▄▄▄  ") 
print("   █    █   █    ▌          █        ▄▀   █       █    █    █    █     █    ▌   ▄▀    █     █        █    ▌  ") 
print("  ▄▀▄▄▄▄▀  ▄▀▄▄▄▄         ▄▀▄▄▄▄▄▄▀ █   ▄▀      ▄▀   ▄▀      ▀▄▄▄▄▀   ▄▀▄▄▄▄   █     █    ▄▀        ▄▀▄▄▄▄   ") 
print(" █     ▐   █    ▐         █         ▐   ▐       █    █                █    ▐   ▐     ▐   █          █    ▐   ") 
print(" ▐         ▐              ▐                     ▐    ▐                ▐                  ▐          ▐        ") 
print("                                                                                                                            ")    

def registro():

    nombre = input("por favor ingrese su nombre para continuar ")
    bienvenida = f"bienbenido al laberinto de la muerte {nombre}"
    print(bienvenida)

registro()

print("para moverte utiliza:")
print("        ____        ")
print("       ||↑ ||       ")
print("       ||__||       ")
print("       |/__\|       ")
print(" ____   ____   ____ ")
print("||← || ||↓ || ||→ ||")
print("||__|| ||__|| ||__||")
print("|/__\| |/__\| |/__\|")
print(" ")
print(" ____")
print("||↑ ||")
print("||__|| para moverte hacia arriba")
print("|/__\|")
print(" ____")
print("||← ||")
print("||__|| para moverte hacia la izquierda")
print("|/__\|")
print(" ____")
print("||↓ ||")
print("||__|| para moverte hacia abajo")
print("|/__\|")
print(" ____")
print("||→ ||")
print("||__|| para moverte hacia la derecha")
print("|/__\|")
print(" ")


print("para comenzar el juego por favor presione")
print("              ____________")
print("             ||          ||")
print("             || ←-Enter  ||")
print("             ||__        ||")
print("             |/_ |       ||")
print("                ||       ||")
print("                ||_______||")
print("                |/_______\|")

import readchar

def on_enter_pressed():
    print("Enter presionado")

try:
    while True:
        key = readchar.readchar()  # Lee un solo carácter de manera no bloqueante
        if key == '\r':  # '\r' es el carácter Enter
            on_enter_pressed()
            break  # Presionar 'enter' para salir del programa

except KeyboardInterrupt:
    pass  # Manejo de Ctrl+C para salir del programa de manera limpia

import os


def mostrar_laberinto(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in laberinto:
        print("".join(fila))

def convertir_a_matriz(laberinto_str):
    return [list(fila) for fila in laberinto_str.split("\n")]

def main_loop(laberinto, inicio, final):
    px, py = inicio

    while (px, py) != final:
        laberinto[px][py] = 'P'
        mostrar_laberinto(laberinto)

        # Leer tecla de flecha
        ("Presiona una tecla de flecha (↑, ↓, ←, →): ")
        tecla = readchar.readchar()

        # Calcular nueva posición tentativa
        nueva_px, nueva_py = px, py

        if tecla == 'w':
            nueva_px -= 1
        elif tecla == 's':
            nueva_px += 1
        elif tecla == 'a':
            nueva_py -= 1
        elif tecla == 'd':
            nueva_py += 1

        # Verificar si la nueva posición es válida
        if 0 <= nueva_px < len(laberinto) and 0 <= nueva_py < len(laberinto[0]) and laberinto[nueva_px][nueva_py] != '#':
            laberinto[px][py] = '.'
            px, py = nueva_px, nueva_py

    print("¡Felicidades! Has llegado al final del laberinto.")

if __name__ == "__main__":
    laberinto_str = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    laberinto = convertir_a_matriz(laberinto_str)
    inicio = (0, 0)
    final = (len(laberinto) - 1, len(laberinto[0]) - 1)


    main_loop(laberinto, inicio, final)

