-- CREATE DATABASE raspi_waterheater;
-- USE raspi_waterheater;

CREATE TABLE tank_temperatures(
  id SERIAL PRIMARY KEY,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  temperature REAL NOT NULL
);

CREATE TABLE output_temperatures(
  id SERIAL PRIMARY KEY,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  temperature REAL NOT NULL
);

CREATE TABLE desired_temperature(
  id SERIAL PRIMARY KEY,
  temperature REAL NOT NULL
);

INSERT INTO desired_temperature(id, temperature) VALUES (1, 0);
