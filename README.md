# Juego del Ahorcado

Un juego del ahorcado interactivo implementado en Python con interfaz web usando Flask.

## Características

- **Interfaz web**: Juego accesible desde cualquier navegador.
- **Categorías**: Palabras organizadas en categorías (animales, frutas, países, colores).
- **Arte ASCII**: Representación visual del ahorcado que se actualiza con cada error.
- **Validación**: Verificación de entradas y letras ya usadas.
- **Nuevo juego**: Botón para iniciar una nueva partida.
- **Responsive**: Diseño adaptable a diferentes tamaños de pantalla.

## Cómo jugar

### Localmente
Ejecuta el script `app.py` con Python:

```
python app.py
```

Abre tu navegador en `http://127.0.0.1:5000/`

### Desplegado en Vercel
El juego está configurado para desplegarse en Vercel. Una vez subido a GitHub, conecta el repositorio a Vercel para un despliegue automático.

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