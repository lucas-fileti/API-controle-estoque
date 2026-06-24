from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    referencia: str
    nome: str
    preco_venda: float
    categoria: str
    ativo: bool = True
    