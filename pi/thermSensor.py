from w1thermsensor import W1ThermSensor
from settings import tankSensorIds, outputSensorIds


class ThermSensor:
  def __init__(self):
    self.tankSensors = []
    self.outputSensors = []

    for sensor in W1ThermSensor.get_available_sensors():
      if sensor.id in tankSensorIds:
        self.tankSensors.append(sensor)
      elif sensor.id in outputSensorIds:
        self.outputSensors.append(sensor)

  def getOutputTemperature(self):
    temperatures = [s.get_temperature() for s in self.outputSensors]
    return average(temperatures)

  def getTankTemperature(self):
    temperatures = [s.get_temperature() for s in self.tankSensors]
    return average(temperatures)

def average(numbers):
  return sum(numbers) / len(numbers)
