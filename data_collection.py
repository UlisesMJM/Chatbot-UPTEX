
import json
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

# Archivo para almacenar las preguntas
LOG_FILE = "user_questions.json"

def log_question(question):
    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(question)

    with open(LOG_FILE, "w") as file:
        json.dump(data, file)

def analyze_questions():
    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
        question_count = Counter(data)
        return question_count.most_common(10)
    except FileNotFoundError:
        return []

@app.route("/log_question", methods=["POST"])
def log_user_question():
    user_input = request.json.get("message")
    if user_input:
        log_question(user_input)
        return jsonify({"status": "success", "message": "Question logged"}), 200
    return jsonify({"status": "error", "message": "No question provided"}), 400

@app.route("/stats", methods=["GET"])
def get_stats():
    stats = analyze_questions()
    return jsonify({"status": "success", "stats": stats}), 200

if __name__ == "__main__":
    app.run(debug=True)