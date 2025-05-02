from flask import Flask, request, render_template

unidades = Flask(__name__)

@unidades.route('/')
def index():
    return render_template("index.html")

@unidades.route("/procesar", methods=["POST"])
def home():
    resultado = None
    try:
        valor = float(request.form.get('valor'))
    except ValueError:
        resultado = "Por favor ingresa un valor numérico válido para 'valor'."
    
    unidad = request.form.get('unidad')
    opcion = request.form.get('opcion')

    if valor is None or unidad is None or opcion is None:
        resultado = "Por favor proporciona los parámetros 'valor', 'unidad' o 'opcion'."

    if unidad == opcion:
        resultado = "El valor que intenta convertir ya se encuentra en la unidad esperada."
    
    if unidad == 'cm' and opcion == 'm':
        resultado = f"{valor/100} metros"
    elif unidad == 'cm' and opcion == 'ft':
        resultado = f"{valor/30.48} pies"
    elif unidad == 'cm' and opcion == 'in':
        resultado = f"{valor/2.54} pulgadas"

    elif unidad == 'ft' and opcion == 'cm':
        resultado = f"{valor * 30.48} centimetros"
    elif unidad == 'ft' and opcion == 'm':
        resultado = f"{valor / 3.28084} metros"
    elif unidad == 'ft' and opcion == 'in':
        resultado = f"{valor * 12} pulgadas"
    
    elif unidad == 'in' and opcion == 'cm':
        resultado = f"{valor * 2.54} centimetros"
    elif unidad == 'in' and opcion == 'm':
        resultado = f"{valor / 39.3701} metros"
    elif unidad == 'in' and opcion == 'ft':
        resultado = f"{valor / 12} pies"

    print(f"Resultado: {resultado}")

    return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
    unidades.run(host='0.0.0.0', port=5000)
