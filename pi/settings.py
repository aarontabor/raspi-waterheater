'''
This water heater daemon communicates with a server to:
  - post temperature readings for storage and analysis
  - query user-specified temperature settings
'''
# The servers network address (can be IP or a registered DNS)
servername = ''

# The amount of time (in seconds) between communications with the server
heartbeat_seconds = 20


'''
Each DS18B20 temperature sensor has a unique identification number.
Identification numbers can be found by connecting a single sensor to the
raspberry pi and using the provided utility script:
  python queryConnectedThermSensors.py

Identification numbers are encoded in hexadecimal and are generally 12 digits in
length, for example:
  00001234abcd

Fill in the current sensor configuration (between the square brackets - []).
Ensure that identification numbers are:
  - are quoted
  - are comma separated

Example:
  tankSensorIds = ['00001234abcd', '00005678bcde']
  outputSensorIds = ['00001a2b3c4d']
'''
tankSensorIds = []
outputSensorIds = []
