# Templates
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    x = 1321
    y = 2123123
    query = request.args.to_dict()
    return render_template("modelo.html", x=x, y=y)


if __name__ == '__main__':
    app.run(debug=True)
