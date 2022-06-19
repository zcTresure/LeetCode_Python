# Write your MySQL query statement below


SELECT stock_name, sum(CASE WHEN operation = 'Buy' THEN -price else price END) AS capital_gain_loss
FROM Stocks s
GROUP BY stock_name;