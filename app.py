from flask import Flask, request, jsonify

app = Flask(__name__)


databaza = {
    "students": [
        {
            "id": 1,
            "name": "Adrian",
            "surname": "Červenka",
            "nickname": "chilli peppers"
            "img" = "https://www.odzadu.sk/wp-content/uploads/2026/03/adrian-zo-sou-ruza-pre-nevestu.jpg"
        }, {
            "id": 2,
            "name": "Janka",
            "surname": "Špenáová",
            "nickname": None
            "img" = "https://www.stvr.sk/media/a501/image/file/1/1000/janka-pcs.jpg"
        }, {
            "id": 3,
            "name": "Markus",
            "surname": "Martiš",
            "nickname": "cigga"
            "img" = "https://pbs.twimg.com/media/GYpgQMJXQAAtqkP.jpg"
        }, {
            "id": 4,
            "name": "Elizabeth",
            "surname": "RolsRojs",
            "nickname": "queen"
            "img" = "https://www.fotoaparat.cz/storage/pm/05/08/03/126341_574c9.jpg"
        }, {
            "id": 5,
            "name": "Versace",
            "surname": "Klúčenka",
            "nickname": "Gucci"
            "img" = "https://cdn.britannica.com/24/270724-050-ADD7DC96/donatella-versace-2024-vanity-fair-oscar-party-march-10-2024-beverly-hills-california.jpg"
        }, {
            "id": 6,
            "name": "Ctibor",
            "surname": "Cyril",
            "nickname": "Čvajgla"
            "img" = "https://www.asb.sk/wp-content/uploads/2023/01/ASB_05_10_2022_-6-of-9-min-e1669667094611.jpg"
        }, {
            "id": 7,
            "name": "Lukáš",
            "surname": "Sfúkaš",
            "nickname": None
            "img" = "https://upload.wikimedia.org/wikipedia/commons/3/34/Luk%C3%A1%C5%A1_Latin%C3%A1k_2015.jpg"
        }, {
            "id": 8,
            "name": "Roman",
            "surname": "Evka",
            "nickname": "detičky krásne"
            "img" = "https://img.topky.sk/320px/1039568.jpg"
        }, {
            "id": 9,
            "name": "Tomáš",
            "surname": "Maštalír",
            "nickname": "herec"
            "img" =
        }, {
            "id": 10,
            "name": "Patrik",
            "surname": "Vrbovský",
            "nickname": "Rytmus"
            "img" = "https://i1.sndcdn.com/avatars-000003218454-hyqoka-t1080x1080.jpg"
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
