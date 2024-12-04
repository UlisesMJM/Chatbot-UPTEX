from flask import Flask, request, jsonify, render_template
from chatbot_logic import chatbot_response

app = Flask(__name__)

# Mensaje de bienvenida predeterminado
WELCOME_MESSAGE = (
    "¡Hola! Bienvenido al chatbot de la UPTex. Puedes hacerme preguntas como:\n"
    "- ¿Qué carreras ofrece la UPTex?\n"
    "- ¿Cuáles son los requisitos de admisión?\n"
    "- ¿Cuál es el horario de atención?\n"
    "- ¿Cuándo abren las convocatorias?\n"
    "¡Estoy aquí para ayudarte!"
)

@app.route('/')
def home():
    # Renderiza la página principal y pasa el mensaje de bienvenida al frontend
    return render_template('index.html', welcome_message=WELCOME_MESSAGE)

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        # Recibe la consulta del usuario desde el frontend
        user_input = request.json.get("message")
        if user_input:
            # Procesa la respuesta con la lógica del chatbot
            response = chatbot_response(user_input)
            return jsonify({"response": response}), 200
        else:
            # Si no hay mensaje, devuelve un error
            return jsonify({"error": "No se proporcionó ninguna consulta."}), 400
    except Exception as e:
        # Manejo de errores generales
        return jsonify({"error": f"Ha ocurrido un error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
