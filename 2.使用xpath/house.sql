CREATE DATABASE lianjia DEFAULT CHARSET utf8;
SHOW VARIABLES LIKE 'character_set_database';
DROP DATABASE lianjia;
USE lianjia
CREATE TABLE house(
	`title` VARCHAR(100),
	`title_url` VARCHAR(100),
	`unitPrice` VARCHAR(100),
	`totalPrice` VARCHAR(100),
	`houseInfo` VARCHAR(100),
	`houseDetail` VARCHAR(300),
	`communityIntroduct` VARCHAR(300),
	`houseType` VARCHAR(300)
)