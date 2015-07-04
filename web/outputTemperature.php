<?php
require('functions_pgsql.php');

switch($_SERVER{'REQUEST_METHOD'}) {
  case 'GET':
    echo getOutputTemperature();
    break;

  case 'POST':
    $temperature = $_POST{'temperature'};
    setOutputTemperature($temperature);
    break;

  default:
    print 'Something went wrong!';
    break;
}

?>
