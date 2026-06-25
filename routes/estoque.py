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
    
    for item in estoque_atual:
        if item["referencia"] == referencia:
            return item
    return {"mensagem": "Produto não encontrado"}

@router.get("/buscar")
def buscar_estoque (
    referencia: str | None = None,
    cor: str | None = None,
    tamanho: str | None = None
    ):

    resultados = []

    for item in estoque_atual:
        if referencia and item["referencia"] != referencia:
            continue
        if cor and item["cor"].lower() != cor.lower():
            continue
        if tamanho and item["tamanho"].lower() != tamanho.lower():
            continue

        resultados.append(item)
    
    return resultados