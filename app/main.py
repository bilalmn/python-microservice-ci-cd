
from fastapi import FastAPI

app = FastAPI(
    title="Python Microservice",
    version="2.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Python microservice is running",
        "version": "2.0.0",
        "deployment": "Updated through CI/CD"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": "2.0.0"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Demo User",
        "version": "2.0.0"
    }

