# 使用 WHERE 子句和 OR【通过】
select
    name, population, area
from
    world
where
    area >= 3000000 or population >= 25000000;


# 使用 WHERE 子句和 UNION【通过】
SELECT
    name, population, area
FROM
    world
WHERE
    area >= 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population >= 25000000;
