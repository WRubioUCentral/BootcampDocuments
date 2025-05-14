from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo_ = "BootCamp TalentoTech!"
    nombres_ = ["William", "Andrés", "Camila", "Laura"]
    return render_template("index.html", nombres = nombres_, titulo = titulo_)

@app.route("/contacto")
def contacto():
    nombre_ = "Juan Delgado"
    email_ = "juan.delgado@yopmail.com"
    return render_template("contacto.html", nombre = nombre_, email = email_)

if __name__ == "__main__":
    app.run(debug = True)