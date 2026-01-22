SELECT
    SUM(cost) AS cost
FROM sales;

SELECT
    person_id,
    SUM(cost) AS cost
FROM sales
GROUP BY
    person_id
ORDER BY
    person_id;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    SUM(cost) OVER (ORDER BY person_id, year_int, month_int ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_cost
FROM sales
ORDER BY
    person_id,
    year_int,
    month_int;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    SUM(cost) OVER (PARTITION BY person_id ORDER BY year_int, month_int ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_cost
FROM sales
ORDER BY
    person_id,
    year_int,
    month_int;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    ROW_NUMBER() OVER (PARTITION BY person_id ORDER BY cost DESC) AS cost_rank
FROM sales
ORDER BY
    person_id,
    cost_rank;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    RANK() OVER (PARTITION BY person_id ORDER BY cost DESC) AS cost_rank
FROM sales
ORDER BY
    person_id,
    cost_rank;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    DENSE_RANK() OVER (PARTITION BY person_id ORDER BY cost DESC) AS cost_rank
FROM sales
ORDER BY
    person_id,
    cost_rank;

SELECT
    person_id,
    year_int,
    month_int,
    cost,
    AVG(cost) OVER (PARTITION BY person_id ORDER BY year_int, month_int ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS rolling_avg_cost
FROM sales;
