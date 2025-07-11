/*
Used in the Python part of the session.
Sample full set of SQL for the person table.
Can be used for the Python part of the exercises.
The `my_db_app_solution.py` file assumes this is the SQL that has been run in the database.
...and that the `databases/exercises/docker-compose.yml` matches what is running in docker.
*/

DROP TABLE if exists person;

CREATE TABLE person (
   person_id INTEGER GENERATED ALWAYS AS IDENTITY,
   first_name VARCHAR(100) NOT NULL,
   last_name VARCHAR(100) NOT NULL,
   age INTEGER,
   PRIMARY KEY(person_id)
);

ALTER TABLE person
ADD email varchar(255);
