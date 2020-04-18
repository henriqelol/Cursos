# Cookie
from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        resp.set_cookie('testeCookie', request.form['cookie'])
    return resp


@app.route('/getcookie')
def getcookie():
    return '<h1>Valor cookie é: {}</h1>'.format(request.cookies.get('testeCookie'))


if __name__ == '__main__':
    app.run(debug=True)
