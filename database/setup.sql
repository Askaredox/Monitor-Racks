-- -----------------------------------------------------
-- Database Racks
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `Racks`;
USE `Racks` ;

-- -----------------------------------------------------
-- Table `Tipo_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Tipo_usuario` (
  `idTipo_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`idTipo_usuario`)
)



-- -----------------------------------------------------
-- Table `Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(64) NOT NULL,
  `apellido` VARCHAR(64) NOT NULL,
  `correo` VARCHAR(64) NOT NULL UNIQUE,
  `contrasena` VARCHAR(32) NOT NULL,
  `create_time` DATETIME NOT NULL,
  `activar_notif` TINYINT NOT NULL DEFAULT 1,
  `activar_correo` TINYINT NOT NULL DEFAULT 1,
  `Tipo_usuario_idTipo_usuario` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `fk_Usuario_Tipo_usuario`
    FOREIGN KEY (`Tipo_usuario_idTipo_usuario`)
    REFERENCES `Tipo_usuario` (`idTipo_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)



-- -----------------------------------------------------
-- Table `Rack`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Rack` (
  `idRack` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(128) NOT NULL,
  `Usuario_idUsuario` INT NOT NULL,
  PRIMARY KEY (`idRack`),
  CONSTRAINT `fk_Rack_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)



-- -----------------------------------------------------
-- Table `Batea`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Batea` (
  `idBatea` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(128) NOT NULL,
  `temperatura` DOUBLE NOT NULL,
  `encendido` TINYINT NOT NULL,
  `Rack_idRack` INT NOT NULL,
  PRIMARY KEY (`idBatea`),
  INDEX `fk_Batea_Rack1_idx` (`Rack_idRack` ASC) VISIBLE,
  CONSTRAINT `fk_Batea_Rack1`
    FOREIGN KEY (`Rack_idRack`)
    REFERENCES `Rack` (`idRack`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)



-- -----------------------------------------------------
-- Table `Historial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Historial` (
  `idHistorial` INT NOT NULL AUTO_INCREMENT,
  `tiempo` DATETIME NOT NULL,
  `signal` INT NOT NULL,
  `descripcion` VARCHAR(256) NOT NULL,
  `Usuario_idUsuario` INT NOT NULL,
  PRIMARY KEY (`idHistorial`),
  INDEX `fk_Historial_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_Historial_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
