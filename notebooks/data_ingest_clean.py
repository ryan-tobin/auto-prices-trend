import pandas as pd

raw = pd.read_csv('data/raw/automobile_prices_economics_2019_2023.csv')

print(raw.info())
print(raw.isna().sum())

clean = raw.copy()
for col in ['New Price ($)', 'Used Price ($)']:
    clean[col] = clean[col].str.replace(',','').astype(float)
for col in ['Inflation Rate (%)', 'Interest Rate (%)']:
    clean[col] = clean[col].str.rstrip('%').astype(float) / 100

clean['Date'] = pd.to_datetime(clean['Month/Year'], format='%y-%b')
clean = clean.drop(columns=['Month/Year'])

clean.head()

clean.to_csv('data/processed/cleaned.csv', index=False)