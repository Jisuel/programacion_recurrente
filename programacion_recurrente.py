import random

def obtener_numero():
    # Función para obtener un número del usuario, asegurándose de que sea un entero válido
    while True:
        try:
            numero = int(input("Adivina el número: "))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def adivina_el_numero(intentos, numero_secreto):
    # Función principal para el juego de adivinanzas
    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. El número correcto era:", numero_secreto)
        return
    else:
        intento = obtener_numero()

        if intento == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número correctamente!")
        elif intento < numero_secreto:
            print("El número es mayor. Te quedan", intentos - 1, "intentos.")
            adivina_el_numero(intentos - 1, numero_secreto)
        else:
            print("El número es menor. Te quedan", intentos - 1, "intentos.")
            adivina_el_numero(intentos - 1, numero_secreto)

def juego_adivinanza():
    print("¡Bienvenido al Juego de Adivinanzas!")

    # Obtener el rango para el número secreto
    while True:
        try:
            rango_inferior = int(input("Ingresa el rango inferior para el número secreto: "))
            rango_superior = int(input("Ingresa el rango superior para el número secreto: "))
            numero_secreto = random.randint(rango_inferior, rango_superior)
            break
        except ValueError:
            print("Por favor, ingresa números enteros válidos para el rango.")

    # Obtener el número máximo de intentos
    while True:
        try:
            intentos_maximos = int(input("Ingresa el número máximo de intentos: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido para el número de intentos.")

    print(f"\nTienes {intentos_maximos} intentos para adivinar el número secreto en el rango ({rango_inferior} - {rango_superior}). ¡Buena suerte!\n")
    
    # Iniciar el juego
    adivina_el_numero(intentos_maximos, numero_secreto)

if __name__ == "__main__":
    juego_adivinanza()
