from flask import Flask, request

convert = Flask(__name__)

@convert.route('/')
def home(): # Con flask no tengo que poner los argumentos dentro de los parentesis de la función.
    valor_str = request.args.get('valor')
    unidad = request.args.get('unidad')

    if valor_str is None or unidad is None:
        return "Por favor proporciona los parámetros 'valor' y 'unidad' en la URL."
    valor = float(valor_str)

    if unidad == 'C':
        resultado = valor * 9/5 + 32
        return f"{valor}°C(celcius) son {resultado} grados °F(Fahrenheit)"
    
    elif unidad == 'F':
        resultado = (valor - 32) * 5/9
        return f"{valor}°F(Fahrenheit) son {resultado} grados °C(celcius)"
    
    else:
        return "Unidad no válida. Usa 'C' para Celcius o 'F' para Fahrenheit."

if __name__ == "__main__":
    convert.run(host='0.0.0.0', port=5000) 