from flask import Flask

# Inicializa aplicação
app = Flask(__name__)

# Rotas
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Inicia o programa
if __name__ == "__main__":
    app.run(debug=True)