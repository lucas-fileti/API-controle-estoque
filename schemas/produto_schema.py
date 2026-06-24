from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    nome: str
    preco: float
    categoria: str