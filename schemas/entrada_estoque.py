from pydantic import BaseModel
from datetime import date

class EntradaEstoqueSchema(BaseModel):
    data_entrada: date
    referencia: str
    cor: str
    tamanho: str
    quantidade: int
    custo_unitario: float
    