def calcular_retorno_diario(dados):
    dados['retorno_diario'] = dados['preco_fechamento'].pct_change()
    return dados
