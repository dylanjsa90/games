from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users_router

app = FastAPI(title="Games API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
