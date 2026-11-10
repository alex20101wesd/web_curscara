from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/xd">¡lanza una moneda!</a>'

@app.route("/xd")
def lanzar_moneda():
    import random
    resultado = random.choice(['cara', 'cruz'])
    return f'{resultado} <a href="/xd">¡lanzar de nuevo!</a>'
app.run()