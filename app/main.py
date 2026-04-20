from fastapi import FastAPI

app = FastAPI(title="TaskFlow Teams API")

@app.get("/")
def root():
    return {"message": "Taskflow Teams funcionando"}