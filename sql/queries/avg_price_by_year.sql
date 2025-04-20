SELECT
  STRFTIME('%Y', m.date) AS year,
  ROUND(AVG(p.new_price), 2) AS avg_new_price,
  ROUND(AVG(p.used_price), 2) AS avg_used_price
FROM months m
JOIN auto_prices p ON m.month_id = p.month_id
GROUP BY year
ORDER BY year;