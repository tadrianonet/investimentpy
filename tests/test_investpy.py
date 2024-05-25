# aula4/tests/test_investpy.py
import sys
import os
import pytest

# Adicionar o diretório 'aula4' ao caminho do sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from aula4.investpy import obter_dados_acao, calcular_retorno_diario, plotar_dados_acao

@pytest.fixture
def api_key():
    return 'your_api_key'

def test_obter_dados_acao(api_key):
    df = obter_dados_acao('AAPL', api_key)
    assert not df.empty

def test_calcular_retorno_diario(api_key):
    df = obter_dados_acao('AAPL', api_key)
    df = calcular_retorno_diario(df)
    assert 'retorno_diario' in df.columns

def test_plotar_dados_acao(api_key, monkeypatch):
    import matplotlib.pyplot as plt

    def do_nothing(*args, **kwargs):
        pass

    monkeypatch.setattr(plt, 'show', do_nothing)

    df = obter_dados_acao('AAPL', api_key)
    plotar_dados_acao(df)
