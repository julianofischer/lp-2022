from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Minha primeira app flask</h1>
    <p>Hello, world!</p>"""

@app.route("/clientes/")
def clientes():
    return "<h1>Essa é a rota de clientes</h1>"

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5001)