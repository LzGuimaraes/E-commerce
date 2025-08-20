import os
import mercadopago
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

public_key = os.getenv("MERCADOPAGO_PUBLIC_KEY")
token = os.getenv("MERCADOPAGO_ACCESS_TOKEN")


def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)

        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]

    return link_pagamento, id_pagamento
