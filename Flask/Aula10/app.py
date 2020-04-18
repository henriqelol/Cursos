# Enviando dados para o template
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("notas.html")


@app.route("/calculo", methods=["POST"])
def calculo():
    return render_template("calculo.html", total=sum([int(valor) for valor in request.form.to_dict().values()]))


if __name__ == '__main__':
    app.run(debug=True)
