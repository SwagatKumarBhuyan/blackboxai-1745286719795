-- SQL script to create banking transactions table and load data from CSV

CREATE TABLE banking_transactions (
    transaction_id VARCHAR(36) PRIMARY KEY,
    account_id VARCHAR(36),
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount DECIMAL(10, 2),
    merchant VARCHAR(255),
    category VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(10),
    country VARCHAR(50)
);

-- Example COPY command for PostgreSQL to load data from CSV
-- Adjust the file path as needed for your environment

-- COPY banking_transactions(transaction_id, account_id, transaction_date, transaction_type, amount, merchant, category, city, state, country)
-- FROM '/path/to/banking_transactions.csv'
-- DELIMITER ','
-- CSV HEADER;
