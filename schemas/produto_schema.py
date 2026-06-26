from pydantic import BaseModel
from typing import Optional

class ProdutoCriar(BaseModel):
    referencia: str
    nome: str
    categoria: str
    preco_venda: float
    ativo: bool = True

class ProdutoAtualizar(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None 
    preco_venda: Optional[float] = None
    ativo: Optional[bool] = None
    