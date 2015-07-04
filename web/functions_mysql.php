<?php
$db_connection = new mysqli("localhost", "eedtech", "raspberry", "raspi_waterheater");


function getDesiredTemperature() {
  $conn = $GLOBALS{'db_connection'};
  $result = $conn->query("SELECT temperature from desired_temperature where id = 1;");
  $row = $result->fetch_assoc();
  return $row['temperature'];
}

function setDesiredTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  $conn->query("UPDATE desired_temperature SET temperature = " . $temperature . " where id = 1;");
}

function getTankTemperature() {
  return "Pass";
}

function setTankTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  $conn->query("INSERT INTO tank_temperatures(temperature) VALUES (" . $temperature . ");");
}

function getOutputTemperature() {
  return "Pass";
}

function setOutputTemperature($temperature) {
  $conn = $GLOBALS{'db_connection'};
  $conn->query("INSERT INTO output_temperatures(temperature) VALUES (" . $temperature . ");");
}

?>

