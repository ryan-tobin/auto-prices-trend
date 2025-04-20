SELECT
  m.date,
  (p.new_price - p.used_price) AS price_spread
FROM months m
JOIN auto_prices p ON m.month_id = p.month_id
ORDER BY price_spread DESC
LIMIT 5;