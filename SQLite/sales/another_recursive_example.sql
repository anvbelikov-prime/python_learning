WITH RECURSIVE
    min_date_from_stocs AS (
        SELECT
            MIN(dt) as min_dt
        FROM stocks
    ),
    max_date_from_stocs AS (
        SELECT
            MAX(dt) as min_dt
        FROM stocks
    ),
    my_cte(dt) AS (
            SELECT (SELECT * FROM min_date_from_stocs)
            UNION ALL
            SELECT DATE(dt, '+1 day')
            FROM my_cte
            WHERE dt < (SELECT * FROM max_date_from_stocs)
    ),
    joined AS (
        SELECT
            m.dt    AS dt,
            s.price AS price
        FROM my_cte as m
        LEFT JOIN stocks as s ON s.dt == m.dt
    )

SELECT
    dt,
    COALESCE(price, LAG(price, 1) OVER (ORDER BY dt)) AS filled_price
FROM joined;
