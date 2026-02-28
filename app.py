from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: dict = None):
    return {
        "prediction": random.choice(["positive", "negative"]),
        "confidence": round(random.uniform(0.80, 0.95), 3)
    }