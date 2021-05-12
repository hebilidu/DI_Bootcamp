CREATE TABLE orders (
    id SERIAL NOT NULL,
    ord_date DATE DEFAULT '2021-05-10',
    cust_id NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cust_id) REFERENCES,customer (id) ON DELETE CASCADE
);