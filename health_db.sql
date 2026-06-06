CREATE DATABASE health_db;

USE health_db;

CREATE TABLE patients(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    disease VARCHAR(50),
    risk FLOAT
);