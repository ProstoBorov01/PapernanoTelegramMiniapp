import uvicorn

from fastapi import FastAPI
from src.backend.controller.user_controller import router as user_router


app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)