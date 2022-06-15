# Write your MySQL query statement below


SELECT DISTINCT author_id id
FROM Views
where author_id = viewer_id
ORDER BY id DESC;