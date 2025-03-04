import uvicorn
from fastapi import FastAPI
from src.backend.controller.user_controller import router as user_router
from src.backend.data import async_engine, create_tables

app = FastAPI()
app.include_router(user_router)

@app.on_event("startup")
async def on_startup():
    await create_tables(async_engine)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)