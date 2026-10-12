#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file(
    'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ','
)

# Drop the unused column
df = df.drop(columns=['Weighted_Price'])

# Rename and convert the date column
df = df.rename(columns={'Timestamp': 'Date'})
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Use dates as the index
df = df.set_index('Date')

# Fill in missing values
df['Close'] = df['Close'].ffill()

for col in ['High', 'Low', 'Open']:
    df[col] = df[col].fillna(df['Close'])

df[['Volume_(BTC)', 'Volume_(Currency)']] = df[
    ['Volume_(BTC)', 'Volume_(Currency)']
].fillna(0)

# Keep data from 2017 onward
df = df.loc['2017-01-01':]

# Calculate daily values
df = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

print(df)

# Plot each column
df.plot(subplots=True, figsize=(12, 10), title='Bitcoin Daily Statistics')
plt.tight_layout()
plt.show()
