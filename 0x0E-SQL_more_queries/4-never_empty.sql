-- The script creates the table id_not_null 
-- if the table id_not_null exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256)); 
