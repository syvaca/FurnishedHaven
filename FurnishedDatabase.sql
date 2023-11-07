DROP DATABASE if exists FurnishedHaven;
CREATE DATABASE FurnishedHaven;

CREATE TABLE FurnishedHaven.entries (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `style` enum('minimalistic','mid-century-modern','mediterranean','coastal','rustic','vintage') NOT NULL,
  `service` enum('studio','room','apartment','house') NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO FurnishedHaven.entries(name, email, style, service)
VALUES 
("Sofia Vaca", "syvaca@usc.edu", "coastal", "room");
