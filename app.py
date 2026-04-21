from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

documents = [
    "AI in education is growing",
    "Machine learning improves automation",
    "AI impacts jobs",
    "Climate change is serious",
    "Education is changing with technology",
    "AI is transforming healthcare",
    "Automation affects industries",
    "Renewable energy helps climate change",
    "Technology is shaping the future",
    "Data science is important in AI"
]

trendingTopics = [
    "AI Revolution",
    "Climate Crisis",
    "Space Exploration",
    "Quantum Computing",
    "Cyber Security"
]

@app.route("/documents")
def get_documents():
    return jsonify(documents)

@app.route("/trending")
def get_trending():
    return jsonify(trendingTopics)

if __name__ == "__main__":
    app.run(debug=True)