<?php
require('functions.php');

switch($_SERVER{'REQUEST_METHOD'}) {
  case 'GET':
    echo getTankTemperature();
    break;

  case 'POST':
    $temperature = $_POST{'temperature'};
    setTankTemperature($temperature);
    break;

  default:
    print 'Something went wrong!';
    break;
}

?>
