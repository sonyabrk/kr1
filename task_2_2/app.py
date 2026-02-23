from fastapi import FastAPI
from pydantic import BaseModel, field_validator, ValidationError

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

    @field_validator('name')
    @classmethod
    def name_length(cls, v):
        if len(v) < 2 or len(v) > 50:
            raise ValueError('Имя должно быть от 2 до 50 символов')
        return v

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v):
        forbidden = ["кринж", "рофл", "вайб"]
        v_lower = v.lower()
        for word in forbidden:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        if len(v) < 10 or len(v) > 500:
            raise ValueError('Сообщение должно быть от 10 до 500 символов')
        return v

feedbacks = []

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}