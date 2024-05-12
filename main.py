from fastapi import FastAPI
from routes.cliente import router as rota_cliente
from routes.vaga import router as rota_vaga

app = FastAPI()

app.include_router(rota_cliente, prefix='/cliente')
app.include_router(rota_vaga, prefix='/vaga')