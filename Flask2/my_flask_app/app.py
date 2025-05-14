from flask import Flask, render_template

app = Flask(__name__) ##Instanciamos función

@app.route("/")
def home():
    usuario = "Brayan Camilo"
    return render_template("index.html", usuario = usuario)

if __name__ == "__main__":
    app.run(debug = True)