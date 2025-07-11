SELECT * FROM teachers;

SELECT year_group FROM teachers;

SELECT * FROM teachers
WHERE teacher_id = 1;

SELECT class_id, teacher_id FROM teachers
ORDER BY class_id DESC;

SELECT first_name, last_name FROM teachers
WHERE first_name LIKE 'Jo%' AND last_name LIKE '%ith';
