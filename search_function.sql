USE student;

SELECT COUNT(`student id`) FROM `classes` WHERE `student id` = (
	SELECT `student id`
    FROM `student`
    WHERE `name` = '盧弘忠'
);

SELECT `date`, `amount`, `teacher` FROM `classes` WHERE `student id` = (
	SELECT `student id`
    FROM `student`
    WHERE `name` = '林宗翰'
);

SELECT SUM(`amount`) FROM `classes` WHERE `student id` = (
	SELECT `student id`
    FROM `student`
    WHERE `name` = '林宗翰'
);

SELECT * FROM `student` WHERE `name` LIKE '%林%';