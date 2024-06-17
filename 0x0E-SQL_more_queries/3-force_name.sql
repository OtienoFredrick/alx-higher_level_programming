-- A script that creates the table force_name on my mysql server
-- if the table exists, the script should not fail. 

CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256) NOT NULL);
