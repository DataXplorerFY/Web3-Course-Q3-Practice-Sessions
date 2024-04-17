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





def start():
    uvicorn.run("webapp.main:app", host = "127.0.0.1", port=8080, reload= True)
