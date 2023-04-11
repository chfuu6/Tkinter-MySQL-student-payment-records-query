SHOW DATABASES;
USE student;

CREATE TABLE `student`(
	`student id` INT PRIMARY KEY,
    `name` VARCHAR(25),
    `phone number` VARCHAR(120)
);

SELECT * FROM `student`;

CREATE TABLE `classes`(
	`order id` INT AUTO_INCREMENT,
    PRIMARY KEY(`order id`),
    `date` VARCHAR(50),
    `amount` INT,
    `teacher` VARCHAR(10),
    `student id` INT,
    FOREIGN KEY(`student id`) REFERENCES `student`(`student id`)
);
DROP TABLE `classes`;

SELECT * FROM `classes`;