
from fastapi import FastAPI

app = FastAPI(
    title="Python Microservice",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Python microservice is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Demo User"
    }
