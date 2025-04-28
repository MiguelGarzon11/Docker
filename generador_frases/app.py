from flask import Flask
import random

frases = [
	"Docker es un gestor de maquinas virtuales",
	"El dockerfile es un archivo de texto que contiene instrucciones sobre cómo crear una imagen de Docker",
	"Docker te permite desarrollar aplicaciones en tu computadora local y luego moverlas a cualquier entorno"
]

app = Flask(__name__)

@app.route('/')
def frase_aleatoria():
	return random.choice(frases)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
