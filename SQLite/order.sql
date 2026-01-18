WITH cnt_nums AS (
	SELECT
		t.num    AS num,
		COUNT(*) AS cnt
	FROM test AS t
	GROUP BY
		t.num
	ORDER BY
		cnt DESC
),
     d AS (
	SELECT CURRENT_DATE AS dt
),
    final AS (
	SELECT
        	c.num AS num,
        	c.cnt AS cnt,
        	d.dt  AS dt
	FROM cnt_nums AS c
	CROSS JOIN d
)

SELECT *
FROM final; 

