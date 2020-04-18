# criando uma URL dinamicamente
from flask import Flask

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<nome>")
def index(nome=""):
    return "Bem Vindo {}".format(nome)


@app.route("/blog1/")
@app.route("/blog1/<int:postID>")
def blog1(postID=-1):
    if postID >= 0:
        return "Valor: {}".format(postID)
    return "Bem Vindo!"


@app.route("/blog2/")
@app.route("/blog2/<float:postID>")
def blog2(postID=-1):
    if postID >= 0:
        return "Valor Float: {}".format(postID)
    return "Bem Vindo no Float!"


if __name__ == '__main__':
    app.run(debug=True, port="3000")
