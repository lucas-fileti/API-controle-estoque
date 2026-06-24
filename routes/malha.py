from fastapi import APIRouter
from schemas.malha_schema import MalhaSchema

router = APIRouter()

malhas = []

@router.get("/")
def listar_malhas():
    return malhas

@router.post("/")
def cadastrar_malha(malha: MalhaSchema):

    valor_total = malha.kg_comprado * malha.preço_kg

    nova_malha = {
        "data_compra": malha.data_compra,
        "fornecedor": malha.fornecedor,
        "cor": malha.cor,
        "kg_comprado": malha.kg_comprado,
        "preço_kg": malha.preço_kg,
        "valor_total": valor_total
    }
    malhas.append(nova_malha)
    
    return {"mensagem": "Malha criada com sucesso", 
            "malha": nova_malha
            }