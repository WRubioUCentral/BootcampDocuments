from flask import Flask, request
##Instanciamos la app de Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡Bienvenidos!"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        return f'Bienvenido {usuario} al Bootcamp de programación.'
    return '''
        <form method = "post">
        Usuario: <input type = "text" name = "username">
        <br>
        <input type = "submit" value = "Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug = True)


## Ejecutar mediante python app.py