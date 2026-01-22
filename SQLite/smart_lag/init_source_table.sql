CREATE TABLE t (
    id   INTEGER,
    time INTEGER,
    value VARCHAR(10)
);

INSERT INTO t
    (id, time, value)
VALUES
    (1, 1, 'a'),
    (1, 2, NULL),
    (1, 3, NULL),
    (1, 4, 'b'),
    (1, 5, NULL),
    (2, 1, 'c'),
    (2, 2, 'd'),
    (2, 3, NULL);

SELECT
    id,
    time,
    value
FROM t
ORDER BY
    id,
    time;
