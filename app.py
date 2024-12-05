from flask import Flask, request, jsonify, render_template
from chatbot_logic import chatbot_response, question_groups

app = Flask(__name__)

# Mensajes principales
WELCOME_MESSAGE = (
    "¡Hola! Bienvenido al chatbot oficial de la UPTex. Estoy aquí para ayudarte con tus preguntas sobre nuestra oferta educativa y servicios. "
    "Para obtener más información, también puedes visitar la página oficial de la universidad en: https://uptexcoco.edomex.gob.mx/. "
    "Por favor, selecciona una categoría o escribe tu pregunta para comenzar."
)


@app.route('/')
def home():
    return render_template(
        'index.html',
        welcome_message=WELCOME_MESSAGE,
        categories=list(question_groups.keys())
    )

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.json.get("message")
        if user_input:
            response = chatbot_response(user_input)
            return jsonify(response), 200
        else:
            return jsonify({"response": "No se proporcionó ninguna consulta.", "suggestions": []}), 400
    except Exception as e:
        return jsonify({"response": f"Ha ocurrido un error: {str(e)}", "suggestions": []}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
