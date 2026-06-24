from pydantic import BaseModel
from datetime import date

class MalhaSchema(BaseModel):
    data_compra: date
    fornecedor: str
    cor: str
    kg_comprado: float
    preço_kg: float