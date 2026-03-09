# Juego del Ahorcado

Un juego del ahorcado interactivo implementado en Python con interfaz gráfica usando Tkinter.

## Características

- **Interfaz gráfica**: Juego con ventana GUI fácil de usar.
- **Categorías**: Palabras organizadas en categorías (animales, frutas, países, colores).
- **Arte ASCII**: Representación visual del ahorcado que se actualiza con cada error.
- **Validación**: Verificación de entradas y letras ya usadas.
- **Nuevo juego**: Botón para iniciar una nueva partida sin cerrar la aplicación.
- **Mensajes**: Retroalimentación inmediata para aciertos y errores.

## Cómo jugar

Ejecuta el script `ahorcado.py` con Python:

```
python ahorcado.py
```

- Se mostrará una categoría y la palabra oculta con guiones bajos.
- Ingresa letras en el campo de texto y presiona "Adivinar letra" o Enter.
- Tienes 6 intentos para adivinar la palabra completa.
- El ahorcado se dibuja progresivamente con cada error.
- Gana adivinando todas las letras antes de agotar los intentos.

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python en Windows)

## Estructura del código

- `PALABRAS`: Diccionario con listas de palabras por categoría.
- `AHORCADO`: Lista de strings con el arte ASCII para cada etapa.
- `HangmanGame`: Clase principal que maneja la interfaz y la lógica del juego.