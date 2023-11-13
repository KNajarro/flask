from flask import Flask, jsonify, request
from flask_cors import CORS
from mailjet import send_email
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/contacto', methods=['POST'])
def enviar_mensaje():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    telefono = data.get('telefono')
    mensaje = data.get('mensaje')

    try:
        send_email(correo)
        result = {'message': 'Mensaje enviado correctamente'}
    except Exception as e:
        print(e)
        result = {'message': 'Error al enviar el mensaje'}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))


