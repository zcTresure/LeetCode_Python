# Write your MySQL query statement below

UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;


UPDATE salary SET sex=IF(sex='f','m','f');
