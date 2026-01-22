WITH
    t_flagged AS (
        SELECT
            id,
            time,
            value,
            CASE WHEN value IS NOT NULL THEN 1 ELSE 0 END AS flag
        FROM t
        ORDER BY
            id,
            time
    ),

    t_groupped AS (
        SELECT
            id,
            time,
            value,
            flag,
            SUM(flag) OVER (PARTITION BY id ORDER BY time) as group_id
        FROM t_flagged
    )

SELECT
    id,
    time,
    value,
    flag,
    group_id,
    COALESCE(value, MAX(value) OVER (PARTITION BY id, group_id ORDER BY time)) AS filled_value
FROM t_groupped
ORDER BY
    id,
    time;
