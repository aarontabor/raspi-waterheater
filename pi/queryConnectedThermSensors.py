from w1thermsensor import W1ThermSensor


print 'Connected Temperature Sensors:'
for sensor in W1ThermSensor.get_available_sensors():
  print '\t%s' % sensor.id

