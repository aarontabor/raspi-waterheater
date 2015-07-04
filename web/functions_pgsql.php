<?php
$db_connection = pg_connect("user=pi host=localhost password=raspberry dbname=raspi_waterheater");


function getDesiredTemperature() {
  $conn = $GLOBALS{'db_connection'};
  $result = pg_query($conn, "SELECT temperature from desired_temperature where id = 1;");
  $row = pg_fetch_assoc($result);
  return $row['temperature'];
}

function setDesiredTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  pg_query($conn, "UPDATE desired_temperature SET temperature = " . $temperature . " where id = 1;");
}

function getTankTemperature() {
  return "Pass";
}

function setTankTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  pg_query($conn, "INSERT INTO tank_temperatures(temperature) VALUES (" . $temperature . ");");
}

function getOutputTemperature() {
  return "Pass";
}

function setOutputTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  pg_query($conn, "INSERT INTO output_temperatures(temperature) VALUES (" . $temperature . ");");
}

?>

