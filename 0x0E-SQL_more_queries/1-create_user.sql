-- A script that creates the MYSQL server user user_0d_1
--  user_0d_1 should have all the priveleges
-- if the  user_0d_1 already exists, your script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
