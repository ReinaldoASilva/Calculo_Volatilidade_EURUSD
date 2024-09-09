import yfinance as yf
import pandas as pd

# Baixar dados históricos do EUR/USD (moeda base: EUR, cotada em USD)
dados = yf.download('EURUSD=X', period='1y', interval='1d')

# Calcular volatilidade diária
dados['Volatilidade'] = (dados['High'] - dados['Low']) / dados['Adj Close'].shift(1) * 100

# Volatilidade máxima, mínima e média
volatilidade_max = dados['Volatilidade'].max()
volatilidade_min = dados['Volatilidade'].min()
volatilidade_media = dados['Volatilidade'].mean()

# Preço médio do EUR/USD no período
preco_medio = dados['Adj Close'].mean()

# Conversão da volatilidade média em pips
volatilidade_media_pips = (volatilidade_media * preco_medio / 100) * 10000

print(f"Volatilidade Máxima: {volatilidade_max:.2f}%")
print(f"Volatilidade Mínima: {volatilidade_min:.2f}%")
print(f"Volatilidade Média: {volatilidade_media:.2f}%")
print(f"Volatilidade Média em Pips: {volatilidade_media_pips:.2f} pips")