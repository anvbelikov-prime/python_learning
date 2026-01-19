CREATE TABLE countries (
    id   INTEGER     PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    abbr VARCHAR(2)  NOT NULL UNIQUE
);
