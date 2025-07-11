SELECT t.first_name || ' ' || t.last_name AS "Full Name", c.year_group as "Year Group", c.class_name AS "Class"
FROM classes c
JOIN teachers t
ON c.class_id = t.class_id;
