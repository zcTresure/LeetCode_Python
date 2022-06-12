# Write your MySQL query statement below

SELECT customer.name as 'Customers'
FROM customer
WHERE customers.id not in
(
    SELECT customerid FROM orders
);