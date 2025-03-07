from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet")
def greet():
    return {"message": "Hello! Have a great day!"}
