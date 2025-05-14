from flask import Flask, request

app = Flask(__name__)

@app.route('/') ##Ruta raiz ##Decorada
def home(): ##Vista en forma de función
    return 'Página de inicio!'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        constasena = request.form['password']
        
        if usuario == 'admin' and constasena == '1234':
            return f'Bienvenido {usuario}'
        else:
            return 'Usuario o contaseña incorrecta.'

    return '''
        <form method = "post">
            Usuario: <input type = "text" name = "username"><br>
            Contrasena: <input type = "password" name = "password"><br>
            <input type = "submit" value = "Iniciar sesión">
        </form>
        '''

@app.route('/welcome', methods = ['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return f'Bienvenido {nombre}'
    return '''
        <form method = "post">
            Usuario: <input type = "text" name = "username"><br>
            <input type = "submit" value = "Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug = True)