# Write your MySQL query statement below

-- IF(Bool表达式,为真返回,为假返回)
SELECT u.name, if(SUM(r.distance) IS NULL, 0, SUM(r.distance)) AS travelled_distance
FROM Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name;


-- COALESCE(表达式1 不为null返回,否则返回表达式2,以此类推)
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name;