from fastapi import FastAPI
from routes.categorias import router as categorias_router

app = FastAPI(
    title="API Stock Control",
    description="API para controle de estoque",
    version="1.0.0"
)

app.include_router(
    categorias_router,
    prefix="/api",
    tags=["Categorias"]
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}
