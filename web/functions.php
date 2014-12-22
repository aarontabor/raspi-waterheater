<?php
$desiredTemperature_filename = '/tmp/.desiredTemperature';
$tankTemperature_filename = '/tmp/.tankTemperature';

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
  $file = fopen($GLOBALS{'tankTemperature_filename'}, 'r');
  $temperature = fgets($file);
  fclose($file);
  return $temperature;
}

function setTankTemperature($temperature) {
  $file = fopen($GLOBALS{'tankTemperature_filename'}, 'w');
  fwrite($file, $temperature);
  fclose($file);
}
?>

