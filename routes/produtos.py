from fastapi import APIRouter
from schemas.produto_schema import ProdutoSchema

router = APIRouter()

produtos = []

@router.get("/")
def listar_produtos():
    return produtos

@router.post("/")
def criar_produto(produto: ProdutoSchema):
    produtos.append(produto)
    return {"mensagem": "Produto criado com sucesso", 
            "produto": produto
            }