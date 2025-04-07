CREATE DATABASE clean_database;

CREATE TABLE clean_database.users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age SMALLINT NOT NULL
);