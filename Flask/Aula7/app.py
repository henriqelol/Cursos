# Objetos de requisição
from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    print("{} --- {}".format(request.method, request.args))
    d1 = request.args.to_dict()
    d2 = dict(request.args)
    dado1 = "D1: {} <br> D2: {}".format(d1, d2)
    dado2 = json.dumps([d1['nome'], d2['idade']])
    return dado1 + "<br><br>" + dado2


if __name__ == '__main__':
    app.run(debug=True)
