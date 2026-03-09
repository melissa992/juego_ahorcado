import tkinter as tk
import random

# Palabras
palabras = ["colombia", "mexico", "canada", "brasil", "argentina"]

palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 6

# -------- FUNCIONES --------

def actualizar_palabra():
    texto = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            texto += letra + " "
        else:
            texto += "_ "

    palabra_label.config(text=texto)

    letras_usadas_label.config(
        text="Letras usadas: " + ", ".join(letras_adivinadas)
    )

    if "_" not in texto:
        resultado_label.config(text="🎉 ¡Ganaste!", fg="green")


def adivinar():
    global intentos

    letra = entrada.get().lower()
    entrada.delete(0, tk.END)

    if letra and letra not in letras_adivinadas:

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos -= 1

        intentos_label.config(text=f"Intentos restantes: {intentos}")

        actualizar_palabra()

        if intentos == 0:
            resultado_label.config(
                text=f"❌ Perdiste. La palabra era: {palabra}", fg="red"
            )


def nuevo_juego():
    global palabra, letras_adivinadas, intentos

    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    intentos_label.config(text="Intentos restantes: 6")
    resultado_label.config(text="")

    actualizar_palabra()


# -------- VENTANA --------

ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("500x500")
ventana.configure(bg="#1e1e2f")

titulo = tk.Label(
    ventana,
    text="🎮 JUEGO DEL AHORCADO",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)

titulo.pack(pady=20)

categoria = tk.Label(
    ventana,
    text="Categoría: Países",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)

categoria.pack()

palabra_label = tk.Label(
    ventana,
    text="",
    font=("Arial", 28, "bold"),
    bg="#1e1e2f",
    fg="#00e5ff"
)

palabra_label.pack(pady=20)

intentos_label = tk.Label(
    ventana,
    text="Intentos restantes: 6",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)

intentos_label.pack()

letras_usadas_label = tk.Label(
    ventana,
    text="Letras usadas:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)

letras_usadas_label.pack(pady=10)

entrada = tk.Entry(
    ventana,
    font=("Arial", 14),
    justify="center"
)

entrada.pack(pady=10)

boton_adivinar = tk.Button(
    ventana,
    text="Adivinar letra",
    font=("Arial", 12, "bold"),
    bg="#00b894",
    fg="white",
    width=15,
    command=adivinar
)

boton_adivinar.pack(pady=5)

boton_nuevo = tk.Button(
    ventana,
    text="Nuevo juego",
    font=("Arial", 12, "bold"),
    bg="#0984e3",
    fg="white",
    width=15,
    command=nuevo_juego
)

boton_nuevo.pack(pady=5)

resultado_label = tk.Label(
    ventana,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)

resultado_label.pack(pady=20)

actualizar_palabra()

ventana.mainloop()
