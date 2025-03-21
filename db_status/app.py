from flask import Flask

app = Flask(__name__)

@app.route('/Harold-Rodriguez/')
def home():
    return "¡Hola desde Flask con Traefik!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

