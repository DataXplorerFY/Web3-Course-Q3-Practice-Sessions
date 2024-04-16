from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/home")
def HelloWorld():
    return "This is home page"



@app.get("/about")
def about():
    return "Hi i am software engineer with a keen interest in AI"


@app.post("/contact/ {id}")
def contactUs(id:int):
    return id



def start():
    uvicorn.run("webapp.main:app", host = "127.0.0.1", port=8080, reload= True)
