import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    ## Datos para el gráfico
    perfil_usario = {
        "nombre":"Carlos",
        "email":"calos.cun@yopmail.com",
        "edad":"27",
        "ciudad": "Bogotá D.C."
    }

    x = [1, 2, 3, 4]
    y = [1, 10, 5, 3]

    ## Creamos el gráfico
    plt.figure(figsize=(6, 4))
    plt.subplot(121)
    plt.grid()
    plt.plot(x, y, 'r--')
    plt.title("Gráfico de ejemplo")
    plt.xlabel("Tiempo(seg)")
    plt.ylabel("Frecuencia")

    plt.subplot(122)
    plt.bar(x, y)
    plt.title("Gráfico de ejemplo")
    plt.xlabel("Tiempo(seg)")
    plt.ylabel("Frecuencia")
    ##Guardamos el gráfico
    buf = io.BytesIO()
    plt.savefig(buf, format = "png")
    buf.seek(0)

    imagen = base64.b64encode(buf.getvalue()).decode('utf8')

    return render_template("index3.html", imagen = imagen, usuario = perfil_usario)

if __name__ == '__main__':
    app.run(debug = True)