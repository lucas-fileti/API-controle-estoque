from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    referencia = Column(String, unique=True, index=True)
    nome = Column(String)
    categoria = Column(String)
    preco_venda = Column(Float)
    ativo = Column(Boolean, default=True)
 
