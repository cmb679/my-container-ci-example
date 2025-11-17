from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Container World!"}

@app.get("/add")
def add(a: int, b: int):
    """Example endpoint to add two numbers."""
    return {"result": a + b}