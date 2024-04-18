from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/home")
def HelloWorld():
    return "home page"



@app.get("/about")
def about():
    return "Hi i am software engineer with a keen interest in AI"


@app.get("/contact/{id}")
def contactUs(id):
    return {"The id enter by the user ": id}

@app.post("/Login")
def login(username: str , password: int ):
    result = {"userName": username, "password": password}
    return result

@app.post("/sum")
def sum(num1:int, num2:int):
    result = num1+num2
    return result





students = []

@app.post("/students")
def create_students(name:str, age:int, grade:str):
    student_id = len(students)+1
    newStudents = {
        "student_id":student_id,
        "name": name,
        "age": age,
        "grade":grade

    }
    students.append(newStudents)
    return newStudents


@app.get("/students")
def Allstudents():
    return students

@app.get("/students/{student_id}")
def getStudent(student_id:int):
    for student in students:
        if student["student_id"] == student_id:
            return student
#* PUT /students/{student_id}: Update a student's details.
@app.put("/students/{student_id}")
def recordUpdate(student_id:int, name:str, age:int, grade:str):
    for student in students:
        if student["student_id"] == student_id:
            student["name"]=name
            student["age"]=age
            student["grade"]=grade
            return student
            



def start():
    uvicorn.run("webapp.main:app", host = "127.0.0.1", port=8080, reload= True)
