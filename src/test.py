import pandas as pd

df = pd.read_csv("../data/AAPL_raw.csv", header=0, skiprows=[1, 2])
df.rename(columns={df.columns[0]: 'Date'}, inplace=True)
print(df.head())