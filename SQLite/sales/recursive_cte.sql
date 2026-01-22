WITH
    RECURSIVE my_cte(n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1
        FROM my_cte
        WHERE n < 10
    )

SELECT *
FROM my_cte;
