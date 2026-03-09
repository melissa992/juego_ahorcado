import random

def elegir_palabra():
    palabras = ["python", "programacion", "ahorcado", "computadora", "teclado"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    print("¡Bienvenido al Juego del Ahorcado!")
    print("La palabra tiene", len(palabra), "letras.")
    
    while intentos > 0:
        print("\n" + mostrar_tablero(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos)
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            print("¡Correcto!")
            if all(l in letras_adivinadas for l in palabra):
                print("\n¡Felicidades! Adivinaste la palabra:", palabra)
                return
        else:
            intentos -= 1
            print("Incorrecto.")
    
    print("\n¡Perdiste! La palabra era:", palabra)

if __name__ == "__main__":
    jugar()