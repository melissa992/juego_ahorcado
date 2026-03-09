import random
import tkinter as tk
from tkinter import messagebox

# Lista de palabras por categorías
PALABRAS = {
    "animales": ["gato", "perro", "elefante", "leon", "tigre", "oso", "conejo", "pajaro"],
    "frutas": ["manzana", "banana", "naranja", "uva", "pera", "sandia", "melon", "fresa"],
    "paises": ["espana", "francia", "italia", "alemania", "mexico", "argentina", "brasil", "colombia"],
    "colores": ["rojo", "azul", "verde", "amarillo", "negro", "blanco", "morado", "rosa"]
}

# Arte ASCII del ahorcado
AHORCADO = [
    """
     +---+
     |   |
         |
         |
         |
         |
=========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
=========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
=========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
=========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
=========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
=========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
========="""
]

def elegir_palabra():
    categoria = random.choice(list(PALABRAS.keys()))
    palabra = random.choice(PALABRAS[categoria])
    return palabra, categoria

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego del Ahorcado")
        self.geometry("400x600")

        # Variables del juego
        self.palabra, self.categoria = elegir_palabra()
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.intentos = 6

        # Widgets
        self.art_label = tk.Label(self, text=AHORCADO[0], font=("Courier", 10), justify=tk.LEFT)
        self.art_label.pack(pady=10)

        self.category_label = tk.Label(self, text=f"Categoría: {self.categoria}", font=("Arial", 12))
        self.category_label.pack()

        self.word_label = tk.Label(self, text=mostrar_tablero(self.palabra, self.letras_adivinadas), font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.attempts_label = tk.Label(self, text=f"Intentos restantes: {self.intentos}", font=("Arial", 12))
        self.attempts_label.pack()

        self.used_label = tk.Label(self, text=f"Letras usadas: {', '.join(sorted(self.letras_usadas))}", font=("Arial", 12))
        self.used_label.pack(pady=5)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.entry.focus()

        self.guess_button = tk.Button(self, text="Adivinar letra", command=self.guess, font=("Arial", 12))
        self.guess_button.pack(pady=5)

        self.new_game_button = tk.Button(self, text="Nuevo juego", command=self.new_game, font=("Arial", 12))
        self.new_game_button.pack(pady=5)

        self.message_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
        self.message_label.pack(pady=10)

        # Bind enter key
        self.entry.bind("<Return>", lambda event: self.guess())

    def guess(self):
        letra = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            self.message_label.config(text="Ingresa una sola letra.", fg="red")
            return

        if letra in self.letras_adivinadas or letra in self.letras_usadas:
            self.message_label.config(text="Ya adivinaste esa letra.", fg="orange")
            return

        self.letras_usadas.append(letra)

        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
            self.message_label.config(text="¡Correcto!", fg="green")
            if all(l in self.letras_adivinadas for l in self.palabra):
                self.message_label.config(text="¡Felicidades! Ganaste.", fg="green")
                self.guess_button.config(state=tk.DISABLED)
                messagebox.showinfo("¡Ganaste!", f"Adivinaste la palabra: {self.palabra}")
        else:
            self.intentos -= 1
            self.message_label.config(text="Incorrecto.", fg="red")
            if self.intentos == 0:
                self.message_label.config(text=f"¡Perdiste! La palabra era: {self.palabra}", fg="red")
                self.guess_button.config(state=tk.DISABLED)
                messagebox.showinfo("¡Perdiste!", f"La palabra era: {self.palabra}")

        self.update_display()

    def update_display(self):
        self.art_label.config(text=AHORCADO[6 - self.intentos])
        self.word_label.config(text=mostrar_tablero(self.palabra, self.letras_adivinadas))
        self.attempts_label.config(text=f"Intentos restantes: {self.intentos}")
        self.used_label.config(text=f"Letras usadas: {', '.join(sorted(self.letras_usadas))}")

    def new_game(self):
        self.palabra, self.categoria = elegir_palabra()
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.intentos = 6
        self.guess_button.config(state=tk.NORMAL)
        self.message_label.config(text="", fg="red")
        self.update_display()
        self.category_label.config(text=f"Categoría: {self.categoria}")

def main():
    app = HangmanGame()
    app.mainloop()

if __name__ == "__main__":
    main()