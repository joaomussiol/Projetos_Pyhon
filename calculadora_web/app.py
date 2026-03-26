from flask import Flask, render_template, request

app = Flask(__name__)

def calcular(num1, operador, num2):
    if operador == "+":
        return num1 + num2

    elif operador == "-":
        return num1 - num2

    elif operador == "*":
        return num1 * num2

    elif operador == "/":
        if num2 == 0:
            return "Erro: divisão por zero"
        else:
            return num1 / num2
    else:
        return "Operador inválido"


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            operador = request.form["operador"]
            num2 = float(request.form["num2"])

            resultado = calcular(num1, operador, num2)

        except ValueError:
            resultado = "Insira apenas valores válidos"

    return render_template("index.html", resultado=resultado)


app.run(debug=True)
