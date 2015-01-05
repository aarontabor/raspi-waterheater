'''
Each DS18B20 temperature sensor has a unique identification number.
Identification numbers can be found by connecting a single sensor to the
raspberry pi and using the provided utility script:
  python queryConnectedThermSensors.py

Identification numbers are encoded in hexadecimal and are generally 11 digits in
length, for example:
  0001234abcd

Fill in the current sensor configuration (between the square brackets - []).
Ensure that identification numbers are:
  - are quoted
  - are comma separated

Example:
  tankSensorIds = ['0001234abcd', '0005678bcde']
  mixSensorIds = ['0001a2b3c4d']
'''
tankSensorIds = []
mixSensorIds = []
