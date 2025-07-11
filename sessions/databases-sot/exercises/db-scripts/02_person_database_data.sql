/*
Used in the Python part of the session.
Sample full set of SQL for the person table.
Can be used for the Python part of the exercises.
The `my_db_app_solution.py` file assumes this is the SQL that has been run in the database.
...and that the `databases/exercises/docker-compose.yml` matches what is running in docker.
*/

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Jane', 'Bloggs', 32, 'jane@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Alice', 'Babbs', 45, 'alice@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Mark', 'Smith', 51, 'mark@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Grace', 'Matthews', 68, 'grace@email.com');

SELECT * FROM person ORDER BY person_id ASC;
