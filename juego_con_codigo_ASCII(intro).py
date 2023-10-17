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

print("presiona")
print(" ____")
print("||↑ ||")
print("||__||")
print("|/__\|")
import readchar

# Bucle infinito para leer y procesar caracteres del teclado
while True:
    key2 = readchar.readchar()  # Lee un caracter del teclado

    # Verifica si se ha presionado la tecla de flecha hacia arriba (UP)
    if key2 == 'H':
        print("Tecla UP presionada. Saliendo del programa.")
        break

    # Imprime el caracter leído
    print(f"Caracter leído: {key2}")

# Cierra el programa
