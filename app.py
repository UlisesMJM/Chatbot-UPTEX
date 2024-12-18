from flask import Flask, request, jsonify, render_template
from chatbot_logic import chatbot_response, question_groups

app = Flask(__name__)

# Mensajes principales

@app.route('/')
def home():
    return render_template(
        'index.html',
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
