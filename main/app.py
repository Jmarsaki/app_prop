# app.py (Backend - Flask) para propinas

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos temporal para almacenar propinas
propinas_db = {}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transferir', methods=['POST'])
def transferir():
    if request.method == 'POST':
        nombre_receptor = request.form['nombre_receptor']
        monto = float(request.form['monto'])

        # Verificar si el receptor existe en la base de datos
        if nombre_receptor in propinas_db:
            propinas_db[nombre_receptor] += monto
        else:
            propinas_db[nombre_receptor] = monto

        return redirect(url_for('index'))


@app.route('/ver_propinas')
def ver_propinas():
    return render_template('ver_propinas.html', propinas=propinas_db)


if __name__ == '__main__':
    app.run(debug=True)