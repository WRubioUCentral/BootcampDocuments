from flask import Flask, render_template

app = Flask(__name__)

@app.route("/main")
def principal():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

if __name__ == "__main__":
    app.run(debug = True)

##Comentario de prueba