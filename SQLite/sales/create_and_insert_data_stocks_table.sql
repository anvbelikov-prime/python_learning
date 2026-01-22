CREATE TABLE stocks (
    dt DATE,
    price DECIMAL
);

INSERT INTO stocks
    (dt, price)
VALUES
    ('2025-01-01', 668.27),
    ('2025-01-03', 678.83),
    ('2025-01-04', 635.40),
    ('2025-01-06', 591.01);

SELECT
    dt,
    price
FROM stocks
ORDER BY
    dt;

