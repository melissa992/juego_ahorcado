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
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
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
        self.geometry("450x650")
        self.configure(bg="#1e1e2f")

        # Variables del juego
        self.palabra, self.categoria = elegir_palabra()
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.intentos = 6

        # ---------- TITULO ----------
        titulo = tk.Label(
            self,
            text="🎮 JUEGO DEL AHORCADO",
            font=("Arial", 22, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        titulo.pack(pady=15)

        # ---------- AHORCADO ----------
        self.art_label = tk.Label(
            self,
            text=AHORCADO[0],
            font=("Courier", 12),
            justify=tk.LEFT,
            bg="#1e1e2f",
            fg="#00e5ff"
        )
        self.art_label.pack(pady=10)

        # ---------- CATEGORIA ----------
        self.category_label = tk.Label(
            self,
            text=f"Categoría: {self.categoria}",
            font=("Arial", 14, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.category_label.pack()

        # ---------- PALABRA ----------
        self.word_label = tk.Label(
            self,
            text=mostrar_tablero(self.palabra, self.letras_adivinadas),
            font=("Arial", 30, "bold"),
            bg="#1e1e2f",
            fg="#00e5ff"
        )
        self.word_label.pack(pady=20)

        # ---------- INTENTOS ----------
        self.attempts_label = tk.Label(
            self,
            text=f"Intentos restantes: {self.intentos}",
            font=("Arial", 14),
            bg="#1e1e2f",
            fg="white"
        )
        self.attempts_label.pack()

        # ---------- LETRAS USADAS ----------
        self.used_label = tk.Label(
            self,
            text=f"Letras usadas: {', '.join(sorted(self.letras_usadas))}",
            font=("Arial", 12),
            bg="#1e1e2f",
            fg="#cccccc"
        )
        self.used_label.pack(pady=10)

        # ---------- ENTRADA ----------
        self.entry = tk.Entry(
            self,
            font=("Arial", 16),
            justify="center",
            width=5
        )
        self.entry.pack(pady=10)
        self.entry.focus()

        # ---------- BOTONES ----------
        botones_frame = tk.Frame(self, bg="#1e1e2f")
        botones_frame.pack(pady=10)

        self.guess_button = tk.Button(
            botones_frame,
            text="Adivinar letra",
            command=self.guess,
            font=("Arial", 12, "bold"),
            bg="#00b894",
            fg="white",
            width=15,
            relief="flat",
            cursor="hand2"
        )
        self.guess_button.grid(row=0, column=0, padx=10)

        self.new_game_button = tk.Button(
            botones_frame,
            text="Nuevo juego",
            command=self.new_game,
            font=("Arial", 12, "bold"),
            bg="#0984e3",
            fg="white",
            width=15,
            relief="flat",
            cursor="hand2"
        )
        self.new_game_button.grid(row=0, column=1, padx=10)

        # ---------- MENSAJES ----------
        self.message_label = tk.Label(
            self,
            text="",
            font=("Arial", 13, "bold"),
            bg="#1e1e2f",
            fg="red"
        )
        self.message_label.pack(pady=15)

        # ENTER para jugar
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
