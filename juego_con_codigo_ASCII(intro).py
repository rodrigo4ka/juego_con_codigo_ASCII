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

def clear_terminal():
    # Función para borrar la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Iniciar con un número en 0
    numero = 0

    # Bucle para leer la tecla 'n' y actualizar el número hasta llegar a 50
    while numero <= 50:
        # Borrar la terminal e imprimir el nuevo número
        clear_terminal()
        print("Número:", numero)

        # Leer la tecla 'n' del teclado
        print("Presiona 'n' para continuar: ")
        input_key = readchar.readchar()
        # Verificar si se presionó la tecla 'n'
        if input_key  == 'n':
            numero += 1
        else:
            print("Tecla incorrecta. Presiona 'n' para continuar.")

if __name__ == "__main__":
    main()

