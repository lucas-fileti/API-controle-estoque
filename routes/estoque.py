from fastapi import APIRouter

router = APIRouter()

estoque_atual = []

@router.get("/")
def listar_estoque():
    return estoque_atual

@router.get("/resumo")
def resumo_estoque():
    total_pecas = 0
    valor_total_custo = 0

    for item in estoque_atual:
        total_pecas += item["quantidade"]
        valor_total_custo += item["quantidade"] * item["custo_unitario"]

    return {
        "total_pecas": total_pecas,
        "valor_total_custo": valor_total_custo
    }