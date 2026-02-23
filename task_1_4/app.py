from fastapi import FastAPI
from models import User

app = FastAPI()

@app.get("/users")
async def get_user():
    user = User(name="Ваше Имя и Фамилия", id=1)
    return user