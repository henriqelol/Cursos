# Construção de URL
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/admin")
def admin():
    return "Bem Vindo Senhor Supremo Admin"


@app.route("/guest/<guest>")
def guest(guest):
    return '<p> Olá guest <b>%s</b></p> ' % guest


@app.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    return redirect(url_for('guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True, port="3000")
