import pandas as pd

# Load data and make day of the weeks
df = pd.read_csv("../data/AAPL_raw.csv", parse_dates=True, header=0, skiprows=[1, 2])
df.rename(columns={df.columns[0]: 'Date'}, inplace=True)
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df['Day'] = df.index.day_name()

# One-Hot encode day of the week
day_dummies = pd.get_dummies(df['Day'], prefix='Day')
df = pd.concat([df, day_dummies], axis=1)

# Getting rid of nans from shifting
df.dropna(inplace=True)

df.to_csv("../data/AAPL_engineered.csv")
print("Saving engineered data to AAPL_engineered.csv")