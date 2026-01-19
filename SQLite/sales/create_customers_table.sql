CREATE TABLE customers(
    id         INTEGER     PRIMARY KEY,
    name       VARCHAR(20) NOT NULL,
    comment    VARCHAR(20) NULL,
    manager_id INTEGER     DEFAULT 0,
    country_id INTEGER     NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries (id),
    CONSTRAINT not_default_name CHECK (LOWER(name) NOT IN ('default', 'default_name', 'no_name', 'no'))
);
