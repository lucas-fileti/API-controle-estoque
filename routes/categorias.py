from fastapi import APIRouter
from schemas.categoria_schema import CategoriaSchema

router = APIRouter()

categorias = []

@router.get("/")
def listar_categorias():
    return categorias

@router.post("/")
def criar_categoria(categoria: CategoriaSchema):
    categorias.append(categoria)
    return {"mensagem": "Categoria criada com sucesso", 
            "categoria": categoria
            }