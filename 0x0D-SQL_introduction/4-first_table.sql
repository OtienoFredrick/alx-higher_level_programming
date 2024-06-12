-- The script creates a table called first table
-- in the current database in the mysql server
-- if the table exists the script should not fail

CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
