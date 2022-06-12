# Write your MySQL query statement below

SELECT user_id,
CONCAT(Upper(left(name,1)),Lower(substring(name,2))) name
FROM users
ORDER BY user_id;