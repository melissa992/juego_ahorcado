// Arte ASCII del ahorcado
const AHORCADO = [
    "+---+\n|   |\n    |\n    |\n    |\n    |\n=========",
    "+---+\n|   |\nO   |\n    |\n    |\n    |\n=========",
    "+---+\n|   |\nO   |\n|   |\n    |\n    |\n=========",
    "+---+\n|   |\nO   |\n/|  |\n    |\n    |\n=========",
    "+---+\n|   |\nO   |\n/|\\ |\n    |\n    |\n=========",
    "+---+\n|   |\nO   |\n/|\\ |\n/   |\n    |\n=========",
    "+---+\n|   |\nO   |\n/|\\ |\n/ \\ |\n    |\n========="
];

let palabra = '';
let categoria = '';
let letrasAdivinadas = [];
let letrasUsadas = [];
let intentos = 6;

document.addEventListener('DOMContentLoaded', function() {
    iniciarJuego();
    
    document.getElementById('guess-btn').addEventListener('click', adivinar);
    document.getElementById('new-game-btn').addEventListener('click', iniciarJuego);
    document.getElementById('letter-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            adivinar();
        }
    });
});

function iniciarJuego() {
    fetch('/new_game')
        .then(response => response.json())
        .then(data => {
            palabra = data.palabra;
            categoria = data.categoria;
            letrasAdivinadas = [];
            letrasUsadas = [];
            intentos = 6;
            
            actualizarDisplay();
            document.getElementById('message').textContent = '';
            document.getElementById('letter-input').focus();
        });
}

function adivinar() {
    const letraInput = document.getElementById('letter-input');
    const letra = letraInput.value.toLowerCase().trim();
    letraInput.value = '';
    
    if (letra.length !== 1 || !letra.match(/[a-z]/)) {
        mostrarMensaje('Ingresa una sola letra.', 'error');
        return;
    }
    
    if (letrasAdivinadas.includes(letra) || letrasUsadas.includes(letra)) {
        mostrarMensaje('Ya adivinaste esa letra.', 'info');
        return;
    }
    
    letrasUsadas.push(letra);
    
    if (palabra.includes(letra)) {
        letrasAdivinadas.push(letra);
        mostrarMensaje('¡Correcto!', 'success');
        
        if (palabra.split('').every(l => letrasAdivinadas.includes(l))) {
            mostrarMensaje('¡Felicidades! Ganaste.', 'success');
            document.getElementById('guess-btn').disabled = true;
        }
    } else {
        intentos--;
        mostrarMensaje('Incorrecto.', 'error');
        
        if (intentos === 0) {
            mostrarMensaje(`¡Perdiste! La palabra era: ${palabra}`, 'error');
            document.getElementById('guess-btn').disabled = true;
        }
    }
    
    actualizarDisplay();
}

function actualizarDisplay() {
    document.getElementById('hangman-art').textContent = AHORCADO[6 - intentos];
    document.getElementById('category').textContent = `Categoría: ${categoria}`;
    document.getElementById('word-display').textContent = mostrarTablero();
    document.getElementById('attempts').textContent = `Intentos restantes: ${intentos}`;
    document.getElementById('used-letters').textContent = `Letras usadas: ${letrasUsadas.sort().join(', ')}`;
    document.getElementById('guess-btn').disabled = intentos === 0 || palabra.split('').every(l => letrasAdivinadas.includes(l));
}

function mostrarTablero() {
    return palabra.split('').map(letra => letrasAdivinadas.includes(letra) ? letra : '_').join(' ');
}

function mostrarMensaje(texto, tipo) {
    const mensaje = document.getElementById('message');
    mensaje.textContent = texto;
    mensaje.className = `message ${tipo}`;
}