CREATE TABLE months (
    month_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL UNIQUE
);

CREATE TABLE auto_prices (
    month_id INTEGER NOT NULL,
    new_price REAL NOT NULL,
    used_price REAL NOT NULL,
    units_sold INTEGER NOT NULL,
    FOREIGN KEY (month_id) REFERENCES months(month_id)
);

CREATE TABLE economics (
    month_id INTEGER NOT NULL,
    inflation_rate REAL NOT NULL,
    interest_rate REAL NOT NULL,
    FOREIGN KEY (month_id) REFERENCES months(month_id)
);

