<?php
$db_connection = new mysqli("localhost", "pi", "raspberry", "raspi_waterheater");

$desiredTemperature_filename = '/tmp/.desiredTemperature';

function getDesiredTemperature() {
  $file = fopen($GLOBALS{'desiredTemperature_filename'}, 'r');
  $temperature = fgets($file);
  fclose($file);
  return $temperature;
}

function setDesiredTemperature($temperature) {
  $file = fopen($GLOBALS{'desiredTemperature_filename'}, 'w');
  fwrite($file, $temperature);
  fclose($file);
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

