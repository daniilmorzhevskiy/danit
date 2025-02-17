from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

def normalize_answer(answer):
    return answer.strip().lower().replace(".", "")

@app.route("/questions", methods=["GET"])
def get_question():
    '''Returns a random question.'''
    question = random.choice(questions)
    return jsonify({
        "id": question["id"],
        "question": question["question"],
        "options": question["options"]
    })

@app.route("/answer", methods=["POST"])
def check_answer():
    'Checks if the submitted answer is correct.'
    data = request.json
    question_id = data.get("id")
    user_answer = data.get("answer")

    question = next((q for q in questions if q["id"] == question_id), None)

    # if not question:
        # return jsonify({"error": "Invalid question ID"}), 400


    correct_option = "ABCD"[question["options"].index(question["answer"])]
    valid_answers = [
        correct_option,
        question["answer"].lower(),
        f"{correct_option}.",
        f"{correct_option}. {question['answer'].lower()}",
        f"{correct_option} {question['answer'].lower()}"
    ]


    if normalize_answer(user_answer) in valid_answers:
        return jsonify({"correct": True, "message": "Correct answer!"})
    else:
        return jsonify({"correct": False, "message": "Wrong answer!"})
    
print("To get question, please, use GET method agoainst the /questions endpoint")
print("To provide an answer, please, use POST method against /answers endpoint")
print("PLEASE BE AWARE that all variants of answers would be valid: A., A. Answer, Answer, answer")

if __name__ == "__main__":
    app.run(debug=False)