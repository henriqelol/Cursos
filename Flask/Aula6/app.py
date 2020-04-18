# Métodos HTTP
from flask import Flask, request
from json import dumps
app = Flask(__name__, static_folder='public')


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        dado = "POST - Nome: {} e Senha: {}<br><br>".format(request.form['nome'], request.form['senha'])
        dado += dumps(request.form)
        return dado
    return "GET"


if __name__ == '__main__':
    app.run(debug=True)
