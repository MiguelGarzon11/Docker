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
    valor = float(request.form.get('valor'))
    unidad = request.form.get('unidad')
    opcion = request.form.get('opcion')

    if valor is None or unidad is None or opcion is None:
        return "Por favor proporciona los parámetros 'valor', 'unidad' o 'opcion'."

    if unidad == opcion:
        return "El valor que intenta convertir ya se encuentra en la unidad esperada."
    if unidad == 'cm' and opcion == 'm':
        resultado = f"El valor en metros de {valor}cm es de: {valor/100} metros."
    elif unidad == 'cm' and opcion == 'ft':
        resultado = f"El valor en pies de {valor}cm es de: {valor/30.48} pies."
    elif unidad == 'cm' and opcion == 'in':
        resultado = f"El valor en pulgadas de {valor}in es de: {valor/2.54} pulgadas."

    elif unidad == 'ft' and opcion == 'cm':
        resultado = f"El valor en centimetros de {valor}ft es de: {valor * 30.48}centimetros."
    elif unidad == 'ft' and opcion == 'm':
        resultado = f"El valor en metros de {valor}ft es de: {valor / 3.28084}metros."
    elif unidad == 'ft' and opcion == 'in':
        resultado = f"El valor en pulgadas de {valor}ft es de: {valor * 12}pulgadas."
    
    elif unidad == 'in' and opcion == 'cm':
        resultado = f"El valor en centimetros de {valor}in es de: {valor * 2.54}centimetros."
    elif unidad == 'in' and opcion == 'm':
        resultado = f"El valor en metros de {valor}in es de: {valor / 39.3701}metros."
    elif unidad == 'in' and opcion == 'ft':
        resultado = f"El valor en pies de {valor}in es de: {valor / 12}pies."
    
    return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
    unidades.run(host='0.0.0.0', port=5000)