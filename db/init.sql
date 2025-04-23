CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO people (name, age) VALUES
('Uttkarsh', 25),
('Dev', 30),
('Prashant', 28);