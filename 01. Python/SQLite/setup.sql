DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT,
    salary REAL
);

INSERT INTO employees (name, position, salary) VALUES ('Alice', 'Manager', 75000);
INSERT INTO employees (name, position, salary) VALUES ('Bob', 'Developer', 60000);
INSERT INTO employees (name, position, salary) VALUES ('Charlie', 'Designer', 55000);
