from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    perfil_usario = {
        "nombre":"Carlos",
        "email":"calos.cun@yopmail.com",
        "edad":"27",
        "ciudad": "Bogotá D.C."
    }
    return render_template("index2.html", perfil = perfil_usario)

if __name__ == "__main__":
    app.run(debug = True)