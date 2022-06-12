# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below


DELETE p1
FROM PERSON p1,
     PERSON p2
WHERE p1.Email = p2.Email
  AND p1.Id > p2.Id;
