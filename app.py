from flask import Flask, request, jsonify

app = Flask(__name__)


databaza = {
    "students": [
        {
            "id": 1,
            "name": "Adrian",
            "surname": "Červenka",
            "nickname": "chilli peppers"
        }, {
            "id": 2,
            "name": "karolína",
            "surname": "Kmeťová",
            "nickname": None
        }, {
            "id": 3,
            "name": "Markus",
            "surname": "Martiš",
            "nickname": "cigga"
        }

    ]
}


@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/student/<int:student_id>")
def find_student(student_id):
    student = databaza["students"][student_id - 1]
    return jsonify(student)


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(databaza)

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in databaza:
        if student["id"] == student_id:
            return jsonify(student)
        
        return jsonify({"error": "Študent nenájdený"}), 404
    
    

@app.route("/")
def home():
    return "Backend beží 🚀"


if __name__ == "__main__":
    app.run(debug=True)

