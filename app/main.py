from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/models")
def get_models():
    return {
        "data": [
            {
                "id": "gemini-2.5-pro",
                "object": "model"
            }
        ]
    }
