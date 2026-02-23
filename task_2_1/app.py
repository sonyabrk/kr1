from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

feedbacks = []

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}