WITH avg_units AS (
  SELECT AVG(units_sold) AS avg_sold FROM auto_prices
)
SELECT
  m.date,
  p.units_sold
FROM months m
JOIN auto_prices p ON m.month_id = p.month_id
WHERE p.units_sold > (SELECT avg_sold FROM avg_units)
ORDER BY p.units_sold DESC;