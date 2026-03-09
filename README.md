# Juego del Ahorcado

Un juego del ahorcado interactivo implementado en Python con interfaz web usando Flask.

## Características

- **Interfaz web**: Juego accesible desde cualquier navegador.
- **Categorías**: Palabras organizadas en categorías (animales, frutas, países, colores).
- **Arte ASCII**: Representación visual del ahorcado que se actualiza con cada error.
- **Validación**: Verificación de entradas y letras ya usadas.
- **Nuevo juego**: Botón para iniciar una nueva partida.
- **Responsive**: Diseño adaptable a diferentes tamaños de pantalla.

## Instalación y Ejecución

### Clonar el repositorio
```bash
git clone https://github.com/melissa992/juego_ahorcado.git
cd juego_ahorcado
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar localmente
```bash
python app.py
```

Abre tu navegador en `http://127.0.0.1:5000/`

## Cómo jugar

- Se mostrará una categoría y la palabra oculta con guiones bajos.
- Ingresa letras en el campo de texto y presiona "Adivinar" o Enter.
- Tienes 6 intentos para adivinar la palabra completa.
- El ahorcado se dibuja progresivamente con cada error.
- Gana adivinando todas las letras antes de agotar los intentos.

## Requisitos

- Python 3.x
- Flask

## Estructura del proyecto

- `app.py`: Servidor Flask principal
- `templates/index.html`: Plantilla HTML del juego
- `static/css/style.css`: Estilos CSS
- `static/js/game.js`: Lógica del juego en JavaScript
- `requirements.txt`: Dependencias de Python
- `vercel.json`: Configuración para despliegue en Vercel

## Despliegue en Vercel

1. Sube este código a un repositorio en GitHub.
2. Ve a [Vercel](https://vercel.com) e importa el proyecto desde GitHub.
3. Vercel detectará automáticamente la configuración y desplegará la aplicación.
4. Obtén la URL del despliegue y comparte el juego.