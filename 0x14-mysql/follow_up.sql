-- create database and table and grant user select priivilege on this table
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE `tyrell_corp`;
CREATE TABLE IF NOT EXISTS `nexus6` (
	`id` INT,
	`name` VARCHAR(256),
);
INSERT INTO `nexus6` (`id`, `name`)
VALUES (1, "Leon");
GRANT SELECT PRIVILEGES ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';
