from fastapi import APIRouter

router = APIRouter()

estoque_atual = []

@router.get("/")
def listar_estoque():
    return estoque_atual
