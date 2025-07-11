INSERT INTO classes (year_group, class_name)
VALUES (4, '4-A');
INSERT INTO classes (year_group, class_name)
VALUES (5, '5-A');
INSERT INTO classes (year_group, class_name)
VALUES (6, '6-A') RETURNING class_id;
