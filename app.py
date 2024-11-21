from flask import Flask,jsonify

app = Flask(__name__)

students = [
    {"id":1,"name":"Dennis","age":20,"Major":"Computer Science"},
    {"id": 2, "name": "Harish", "age": 20, "major": "Mathematics"},
    {"id": 3, "name": "Badri", "age": 20, "major": "Machine Learning"}
]

@app.route("/")
def home():
    return "Hello World"

@app.route("/students",methods=["GET"])
def getStudents():
    return jsonify(students)

@app.route("/students/<int:studentId>",methods=["GET"])
def getStudent(studentId):
    student=None
    for i in students:
        if i["id"]==studentId:
            student=i
            break
    if student!=None:
        return jsonify(student)
    else:
        return jsonify({"error":"Student not found"}),404

if __name__=='__main__':
    app.run("0.0.0.0",5000)