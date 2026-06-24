from fastapi import APIRouter
from schemas.entrada_estoque import EntradaEstoqueSchema
from routes.estoque import estoque_atual

router = APIRouter()

entradas_estoque = []

@router.get("/")
def listar_entradas_estoque():
    return entradas_estoque

@router.post("/")
def criar_entrada_estoque(entrada: EntradaEstoqueSchema):

    valor_total = entrada.quantidade * entrada.custo_unitario

    nova_entrada = {
        'data_entrada': entrada.data_entrada,
        "referencia": entrada.referencia,
        "cor": entrada.cor,
        "tamanho": entrada.tamanho,
        "quantidade": entrada.quantidade,
        "custo_unitario": entrada.custo_unitario,
        "valor_total": valor_total
    }

    entradas_estoque.append(nova_entrada)

    item_encontrado = None

    for item in estoque_atual:
        if (
            item["referencia"] == entrada.referencia and
            item["cor"] == entrada.cor and
            item["tamanho"] == entrada.tamanho
        ):
            item_encontrado = item
            break

    if item_encontrado:
        item_encontrado["quantidade"] += entrada.quantidade
    else:
        novo_item_estoque = {
            "referencia": entrada.referencia,
            "cor": entrada.cor,
            "tamanho": entrada.tamanho,
            "quantidade": entrada.quantidade,
            "custo_unitario": entrada.custo_unitario
        }
        estoque_atual.append(novo_item_estoque)

    return {"mensagem": "Entrada de estoque criada com sucesso", 
            "entrada": nova_entrada,
            "estoque_atual": estoque_atual
            }
    
