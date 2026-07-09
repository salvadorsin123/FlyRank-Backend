from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, FlyRank!", "mensagge!" : "¡Hola, FlyRank!"}

@app.get("/status")
def read_status():
    return {"status": "ok", "fase": "Setup Week 1"}
