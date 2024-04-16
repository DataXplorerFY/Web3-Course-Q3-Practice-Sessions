from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/")
def helloWorld():
    return "Hello This is Home page"








@app.get("/login")
def login_signup(email: str, password: str):
    print("data recieved")
    
    return {"email": email, "password": password}

def start():
    uvicorn.run("app.main:app", host = "127.0.0.1", port = 8080)
