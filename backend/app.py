from flask import Flask, request, jsonify
from scheduler import generate_timetable

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    timetable = generate_timetable(data)
    return jsonify(timetable)

if __name__ == "__main__":
    app.run(debug=True)
