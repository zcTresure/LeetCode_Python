# Write your MySQL query statement below


SELECT event_day day, emp_id, sum(out_time - in_time) total_time
FROM employees
GROUP BY day
ORDER BY day, emp_id;