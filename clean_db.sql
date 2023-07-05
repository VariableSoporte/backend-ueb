DELIMITER //
CREATE PROCEDURE CleanDatabase()
BEGIN
    DELETE FROM candidates;
    DELETE FROM lists_documents;
    DELETE FROM lists;
    DELETE FROM students;
    DELETE FROM courses;    
    UPDATE votes_null SET blank_votes_morning = 0, blank_votes = 0, blank_votes_afternoon = 0,
    null_votes = 0, null_votes_morning = 0, null_votes_afternoon = 0 WHERE id = 1;
    ALTER TABLE courses AUTO_INCREMENT = 1
    ALTER TABLE students AUTO_INCREMENT = 1
    ALTER TABLE lists AUTO_INCREMENT = 1
    ALTER TABLE candidates AUTO_INCREMENT = 1
    ALTER TABLE lists_documents AUTO_INCREMENT = 1
END //
DELIMITER ;