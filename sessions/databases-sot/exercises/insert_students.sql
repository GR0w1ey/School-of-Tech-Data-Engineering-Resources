INSERT INTO students (first_name, last_name, year_group, teacher_id)
VALUES 
    ('Wisam', 'Abdo', 5, 5),
    ('Oluwatamilore', 'Olanpejo', 6, 1)     RETURNING student_id;
