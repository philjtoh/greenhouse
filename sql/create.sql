CREATE DATABASE Greenhouse;
CREATE USER 'Greenhouse.Reader'@'localhost' IDENTIFIED BY 'e463daea5f91438a';
CREATE USER 'Greenhouse.Writer'@'localhost' IDENTIFIED BY '97ad48e2298fbeb9';
CREATE TABLE Greenhouse.Readings (
	ReadingID INT AUTO_INCREMENT NOT NULL,
	ReadingTimestamp DATETIME,
	ReadingAirTemp DECIMAL(4,2),
	ReadingHumidity DECIMAL(4,2),
	ReadingCPUTemp DECIMAL(4,2),
	ReadingPhoto MEDIUMBLOB,
	PRIMARY KEY(ReadingID)
);

GRANT SELECT ON Greenhouse.Readings TO 'Greenhouse.Reader'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON Greenhouse.Readings TO 'Greenhouse.Writer'@'localhost';

