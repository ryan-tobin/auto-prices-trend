from pathlib import Path
import sqlite3 
import pandas as pd

def run_query(conn, path):
    q = Path(path).read_text()
    return pd.read_sql(q, conn)

def main():
    root = Path(__file__).parents[1]
    dbfile = root / 'data' / 'auto_data.db'
    conn = sqlite3.connect(dbfile)

    for qfile in (root / 'sql'/ 'queries').glob("*.sql"):
        print(f"\n--- {qfile.name} ----")
        df = run_query(conn,qfile)
        print(df.to_string(index=False))

    conn.close()

if __name__ == '__main__':
    main()