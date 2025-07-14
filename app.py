from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message")
    if not user_msg:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a friendly AI doctor giving empathetic advice, always suggest to consult a real doctor."},
            {"role": "user", "content": user_msg}
        ]
    )
    answer = response["choices"][0]["message"]["content"].strip()
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
