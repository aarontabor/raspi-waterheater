<?php
require('functions_pgsql.php');

switch($_SERVER{'REQUEST_METHOD'}) {
  case 'GET':
    echo getDesiredTemperature();
    break;

  case 'POST':
    $temperature = $_POST{'temperature'};
    echo $temperature;
    setDesiredTemperature($temperature);
    break;

  default:
    print 'Something went wrong!';
    break;
}

?>
