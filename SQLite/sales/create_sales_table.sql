CREATE TABLE sales (
    order_id  INTEGER PRIMARY KEY,
    person_id INTEGER,
    year_int  INTEGER,
    month_int INTEGER,
    cost      DECIMAL,
    CONSTRAINT sales_person_fk FOREIGN KEY (person_id) REFERENCES persons (id)
);
