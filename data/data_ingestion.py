import yfinance as yf

df = yf.download("AAPL", start="2019-01-01", end="2023-12-31")

df.to_csv("AAPL_raw.csv")
print("Saved raw AAPL data to csv")