CREATE DATABASE raspi_waterheater;
USE raspi_waterheater;

CREATE TABLE tank_temperatures(
  id INT NOT NULL AUTO_INCREMENT,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  temperature DOUBLE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE output_temperatures(
  id INT NOT NULL AUTO_INCREMENT,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  temperature DOUBLE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE desired_temperature(
  id INT NOT NULL,
  temperature DOUBLE NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO desired_temperature(id, temperature) VALUES (1, 0);
