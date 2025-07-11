SELECT * FROM students;

SELECT year_group FROM students;

SELECT * FROM students
WHERE student_id = 1;

SELECT year_group, teacher_id FROM students
ORDER BY year_group DESC;

SELECT first_name, last_name FROM students
WHERE first_name LIKE 'Wi%' AND last_name LIKE '%do';
