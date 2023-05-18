-- creates the table unique_id on your MYSQL server
-- the database name will be passed as an aegument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
