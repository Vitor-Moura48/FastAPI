from fastapi import FastAPI
from routes.cliente import router as rota_cliente

app = FastAPI()

app.include_router(rota_cliente)