INSERT INTO teachers (first_name, last_name, class_id)
VALUES 
    ('John', 'Smith', 3), 
    ('Jane', 'Smith', 2) 
    ('Mike', 'Wazowski', 3) RETURNING teacher_id;
