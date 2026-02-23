from fastapi import FastAPI

app = FastAPI()

@app.post("/calculate")
async def calculate(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}