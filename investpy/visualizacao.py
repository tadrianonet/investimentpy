import matplotlib.pyplot as plt

def plotar_dados_acao(dados):
    plt.figure(figsize=(10, 5))
    plt.plot(dados['data'], dados['preco_fechamento'], marker='o')
    plt.title('Preço de Fechamento da Ação')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.grid(True)
    plt.show()
