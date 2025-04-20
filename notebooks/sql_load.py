from pathlib import Path
import sqlite3
import pandas as pd

def main():
    root = Path(__file__).parents[1]
    dbfile = root / 'data' / 'auto_data.db'
    schema = root / 'sql' / 'schema.sql'
    csv = root / 'data' / 'processed' / 'cleaned.csv'

    conn = sqlite3.connect(dbfile)
    with open(schema) as f:
        conn.executescript(f.read())

    df = pd.read_csv(csv, parse_dates=['Date'])
    df = df.dropna(subset=['Date'])
    month_df = pd.DataFrame({'date': df['Date'].dt.strftime("%Y-%m-%d")})
    month_df.drop_duplicates(inplace=True)
    month_df.to_sql('months', conn, if_exists='append',index=False)

    month_ids = pd.read_sql('SELECT month_id, date FROM months', conn)
    df['month_id'] = df['Date'].dt.strftime("%Y-%m-%d").map(month_ids.set_index('date')['month_id'])

    df['units_sold'] = df['Units Sold'].astype(str).str.replace(',','').astype(int)
    df['inflation_rate'] = df['Inflation Rate (%)'] / 100
    df['interest_rate'] = df['Interest Rate (%)'] / 100

    price_df = df[[
        "month_id",
        "New Price ($)",
        "Used Price ($)",
        "units_sold"
    ]].copy()

    # Rename to match SQL schema
    price_df.columns = [
        "month_id",
        "new_price",
        "used_price",
        "units_sold"
    ]

    # Insert into auto_prices
    price_df.to_sql(
        "auto_prices",
        conn,
        if_exists="append",
        index=False,
        method="multi"
    )
    econ_df = df[["month_id", "inflation_rate", "interest_rate"]]
    econ_df.to_sql("economics", conn, if_exists="append", index=False, method="multi")
    
    conn.close()
    print(f'Data loaded into {dbfile}')

if __name__ == '__main__':
    main()
    