from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict(text: str = ""):
    return {"result": f"Mock AI response for: '{text}'", "confidence": 0.99}
