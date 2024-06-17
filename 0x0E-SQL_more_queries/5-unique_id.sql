-- The script creates the table unique_id 
-- if the table already exists the svript should not fail

CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
