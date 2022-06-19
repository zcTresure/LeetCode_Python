# Write your MySQL query statement below


SELECT u.name AS NAME,SUM(t.amount) AS BALANCE
FROM Users u LEFT JOIN Transactions t
ON u.account = t.account
GROUP BY name
HAVING BALANCE>=10000;
