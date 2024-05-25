# InvestPy

InvestPy é uma biblioteca Python para análise de investimentos. Ela permite obter dados de ações, calcular indicadores financeiros e visualizar gráficos de desempenho.

## Funcionalidades

- Obter dados históricos de ações usando a API do Alpha Vantage.
- Calcular retorno diário das ações.
- Visualizar gráficos de preços de fechamento das ações.

## Requisitos

- Python 3.6+
- pandas
- matplotlib
- requests
- pytest



## Configuração

Obtenha uma chave de API do [Alpha Vantage](https://www.alphavantage.co/support/#api-key) e substitua `'your_api_key'` pela sua chave de API nos exemplos abaixo.


## Uso

Depois de importar a biblioteca com o comando `pip install investimentpy==1.0.0` e já estiver com a sua KEY da *Alpha Vantage*, você pode criar um código como no exemplo a seguir:

```shell
import investpy

api_key = 'SUA_KEY'

# Obter dados de ação
df = investpy.obter_dados_acao('AAPL', api_key)

# Calcular retorno diário
df = investpy.calcular_retorno_diario(df)

# Plotar dados da ação
investpy.plotar_dados_acao(df)

```

Resultado:
![resultado calculo retorno diario](https://raw.githubusercontent.com/tadrianonet/investimentpy/main/exemplo.png)


## Contribuindo

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature/foobar`)
3. Commit suas mudanças (`git commit -am 'Add some feature'`)
4. Push para a branch (`git push origin feature/foobar`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.