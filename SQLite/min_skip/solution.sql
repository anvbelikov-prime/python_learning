WITH
    joined AS (
        SELECT
            t1.id AS initial_id,
            t2.id AS joined_id
        FROM t AS t1
        LEFT JOIN t AS t2 ON t2.id == (t1.id + 1)
    )

SELECT
    MIN(initial_id) + 1 AS answer
FROM joined
WHERE joined_id IS NULL;
