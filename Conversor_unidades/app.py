from flask import Flask, request, render_template

convertir_unidades = Flask(__name__)

unidades = {
    "m" : "metros",
    "cm" : "centimetros",
    "in" : "pulgadas",
    "ft" : "pies"
}
@unidades.route('/')
def index():
    return render_template("index.html")

@unidades.route("/procesar", methods=["POST"])
def home():
    valor_str = request.form.get('valor')
    unidad = request.form.get('unidad')

    if valor_str is None or unidad is None:
        return "Por favor proporciona los parámetros 'valor' y 'unidad'."

    valor = float(valor_str)
