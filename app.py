from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    categoria = random.choice(list(PALABRAS.keys()))
    palabra = random.choice(PALABRAS[categoria])
    return jsonify({
        'palabra': palabra,
        'categoria': categoria,
        'longitud': len(palabra)
    })

if __name__ == '__main__':
    app.run(debug=True)