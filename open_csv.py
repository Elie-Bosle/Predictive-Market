import pandas as pd

df = pd.read_csv('Polymarket_open.csv')

print(df.columns)

for i in range(df.shape[1]):
    print(df.columns[i])