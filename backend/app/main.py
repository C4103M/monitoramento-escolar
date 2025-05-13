from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/exemplo")
def read_root():
    return {"message": "API rodando na porta 5000"}