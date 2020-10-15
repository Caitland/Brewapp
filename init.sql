SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `favourites`;
CREATE TABLE `favourites` (
  `name` varchar(100) NOT NULL,
  `drink` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `favourites` (`name`, `drink`) VALUES
('Giles',	'Coffee');

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `name` varchar(100) NOT NULL,
  `orders` varchar(100) DEFAULT NULL,
  `total` int DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `people`;
CREATE TABLE `people` (
  `User_Name` varchar(100) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Display_Name` varchar(100) DEFAULT NULL,
  `Job_Title` varchar(100) DEFAULT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `Office_Number` int DEFAULT NULL,
  `Phone` int DEFAULT NULL,
  `Mobile_Phone` int DEFAULT NULL,
  `Fax` int DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `ZIP` int DEFAULT NULL,
  `Country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`User_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `receipts`;
CREATE TABLE `receipts` (
  `name` varchar(100) NOT NULL,
  `drinks` varchar(100) DEFAULT NULL,
  `total` int DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
