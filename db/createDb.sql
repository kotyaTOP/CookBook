CREATE SCHEMA `dishdb`;

CREATE TABLE IF NOT EXISTS `dishdb`.`dish` (
`idDish` INT NOT NULL AUTO_INCREMENT,
`DishName` VARCHAR(45) NOT NULL,
`Recipe` varchar(100) NOT NULL,
`Time` time NOT NULL,
PRIMARY KEY (`idDish`));

CREATE TABLE IF NOT EXISTS `dishdb`.`ingredient` (
`idIngred` INT NOT NULL,
`IngredName` VARCHAR(45) NOT NULL,
PRIMARY KEY (`idIngred`));

CREATE TABLE IF NOT EXISTS `dishdb`.`unit` (
`idUnit` INT NOT NULL,
`UnitName` VARCHAR(45) NOT NULL,
PRIMARY KEY (`idUnit`));


CREATE TABLE IF NOT EXISTS `dishdb`.`dishIngred` (
`idDishIngred` INT NOT NULL AUTO_INCREMENT,
`idDish` int NOT NULL,
`idIngred` INT NOT NULL,
`idUnit` int NOT NULL,
`Sum` INT NOT NULL,
PRIMARY KEY (`idDishIngred`),
FOREIGN KEY (`idDish`)
REFERENCES `dishdb`.`dish` (`idDish`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
FOREIGN KEY (`idIngred`)
REFERENCES `dishdb`.`ingredient` (`idIngred`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
FOREIGN KEY (`idUnit`)
REFERENCES `dishdb`.`unit` (`idUnit`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);

