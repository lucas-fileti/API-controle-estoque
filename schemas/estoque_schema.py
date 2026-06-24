from pydantic import BaseModel

class EstoqueSchema(BaseModel):
    produto: str
    quantidade: int
    cor: str
    tamanho: str