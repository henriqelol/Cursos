# Redirecionamento e erros
from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form['nome'] == 'admin' and request.form['senha'] == 'admin':
            return redirect(url_for("sucesso"), code=302)
        abort(401)
    abort(403)


@app.route("/sucesso")
def sucesso():
    return 'sucesso!'


if __name__ == '__main__':
    app.run(debug=True)
