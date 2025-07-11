CREATE TABLE teachers (
  teacher_id INTEGER GENERATED ALWAYS AS IDENTITY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  class_id INTEGER,
  PRIMARY KEY(teacher_id),
  CONSTRAINT fk_class
    FOREIGN KEY(class_id)
    REFERENCES classes(class_id)
);
