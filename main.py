from fastapi import FastAPI
from routes.categorias import router as categorias_router
from routes.produtos import router as produtos_router
from routes.estoque import router as estoque_router
from routes.malha import router as malha_router
from routes.entradas_estoque import router as entradas_estoque_router

app = FastAPI(
    title="API Stock Control",
    description="API para controle de estoque",
    version="1.0.0"
)

app.include_router(
    categorias_router,
    prefix="/categorias",
    tags=["Categorias"]
)

app.include_router(
    produtos_router,
    prefix="/produtos",
    tags=["Produtos"]
)

app.include_router(
    estoque_router,
    prefix="/estoque",
    tags=["Estoque"]
)
    
app.include_router(
    malha_router,
    prefix="/malhas",
    tags=["Malhas"]
)

app.include_router(
    entradas_estoque_router,
    prefix="/entradas-estoque",
    tags=["Entradas de Estoque"]
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}
