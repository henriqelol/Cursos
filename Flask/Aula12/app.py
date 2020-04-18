# Session

from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = "123456"


@app.route('/')
def index():
    usuario = ''
    if 'usuario' in session:
        usuario = session['usuario']
    return render_template('index.html', usuario=usuario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['usuario'] != '':
        session['usuario'] = request.form['usuario']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/setsession/<s>')
def setsession(s):
    session['usuario'] = s;
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
