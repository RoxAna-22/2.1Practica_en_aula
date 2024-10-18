from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_secreto'  # Clave secreta para la sesión

# Datos de usuarios (para ejemplo, pero en producción se usaría una base de datos)
users = {
    "roxana": "123456",
    "admin": "adminpass"
}

@app.route('/')
def index():
    # Si el usuario ya ha iniciado sesión, redirigir a la página de bienvenida
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar si el usuario y la contraseña son correctos
        if username in users and users[username] == password:
            session['username'] = username  # Guardar el usuario en la sesión
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')  # Mensaje de error

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    # Verificar si el usuario ha iniciado sesión
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return redirect(url_for('login'))

@app.route('/cerrar_bienvenida')
def cerrar_bienvenida():
    # Eliminar el usuario de la sesión y redirigir al inicio
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
