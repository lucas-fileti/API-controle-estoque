from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal
from schemas.produto_schema import ProdutoCriar, ProdutoAtualizar
from models.produto_model import Produto

router = APIRouter()

def pegar_banco():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_produtos(db: Session = Depends(pegar_banco)):
    produtos = db.query(Produto).all()
    return produtos

@router.post("/")
def criar_produto(produto: ProdutoCriar, db: Session = Depends(pegar_banco)):

    produto_existente = (
        db.query(Produto)
        .filter(Produto.referencia == produto.referencia)
        .first()
    )
    
    if produto_existente:
        raise HTTPException(
            status_code=400, 
            detail="Referencia já existe"
            )

    novo_produto = Produto(
        referencia=produto.referencia,
        nome=produto.nome,
        categoria=produto.categoria,
        preco_venda=produto.preco_venda,
        ativo=produto.ativo
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return {
        "mensagem": "Produto criado com sucesso",
        "produto": novo_produto
    }

@router.get("/{referencia}")
def buscar_produto(referencia: str, db: Session = Depends(pegar_banco)):
    produto = db.query(Produto).filter(Produto.referencia == referencia).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

