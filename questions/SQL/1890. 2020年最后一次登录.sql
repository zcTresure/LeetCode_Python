# Write your MySQL query statement below


SELECT user_id, MAX(time_stamp) last_stamp
FROM logins
WHERE time_stamp >= '2020-01-01 00:00:00'
  AND time_stamp <= '2020-12-31:23:59:59'
GROUP BY user_id;
