CREATE TABLE classes (
  class_id INTEGER GENERATED ALWAYS AS IDENTITY,
  year_group INTEGER,
  class_name VARCHAR(15),
  PRIMARY KEY(class_id)
);
