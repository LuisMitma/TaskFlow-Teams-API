from fastapi import FastAPI
from app.routers.auths import router as auth_router

app = FastAPI(title="TaskFlow Teams API")
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Taskflow Teams API funcionando"}