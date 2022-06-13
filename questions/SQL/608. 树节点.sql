# Write your MySQL query statement below

# 查找根节点
SELECT id, 'Root' AS Type
FROM tree
WHERE p_id IS NULL;

# 查找内部节点
SELECT id, 'Inner' AS Type
FROM tree
WHERE id IN (SELECT DISTINCT p_id
             FROM tree
             WHERE p_id IS NOT NULL)
  AND p_id IS NOT NULL;


# 查找叶子节点
SELECT id, 'Leaf' AS Type
FROM tree
WHERE id NOT IN (SELECT DISTINCT p_id
                 FROM tree
                 WHERE p_id IS NOT NULL)
  AND p_id IS NOT NULL;


# 合并
SELECT id, 'Root' AS Type
FROM tree
WHERE p_id IS NULL

UNION
SELECT id, 'Inner' AS Type
FROM tree
WHERE id IN (SELECT DISTINCT p_id
             FROM tree
             WHERE p_id IS NOT NULL)
  AND p_id IS NOT NULL

UNION
SELECT id, 'Leaf' AS Type
FROM tree
WHERE id NOT IN (SELECT DISTINCT p_id
                 FROM tree
                 WHERE p_id IS NOT NULL)
  AND p_id IS NOT NULL
ORDER BY id;

# 使用控制语句CASE
SELECT id AS 'Id',
       CASE
           WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
               THEN 'Root'
           WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
               THEN 'Inner'
           ELSE 'Leaf' END AS Type
FROM tree
ORDER BY 'Id';

# 使用IF
SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) Type
FROM
    tree atree
ORDER BY atree.id
