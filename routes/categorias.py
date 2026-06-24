from fastapi import APIRouter

router = APIRouter()

@router.get("/categorias")
def listar_categorias():
    return [
        "Verão",
        "Inverno"
    ]