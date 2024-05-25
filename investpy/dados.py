# investpy/dados.py
import pandas as pd
import requests

def obter_dados_acao(ticker, api_key):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': ticker,
        'apikey': api_key,
        'datatype': 'json'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        raise ValueError("Erro ao obter dados da API")

    time_series = data['Time Series (Daily)']
    dates = []
    close_prices = []

    for date, values in time_series.items():
        dates.append(date)
        close_prices.append(float(values['4. close']))

    df = pd.DataFrame({
        'data': pd.to_datetime(dates),
        'preco_fechamento': close_prices
    })

    df.sort_values('data', inplace=True)
    return df
