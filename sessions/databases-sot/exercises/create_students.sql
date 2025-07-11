CREATE TABLE students (
  student_id INTEGER GENERATED ALWAYS AS IDENTITY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  year_group INTEGER,
  teacher_id INTEGER,
  PRIMARY KEY(student_id),
  CONSTRAINT fk_teacher
    FOREIGN KEY(teacher_id)
    REFERENCES teachers(teacher_id)
);
