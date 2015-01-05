from w1thermsensor import W1ThermSensor
from settings import tankSensorIds, mixSensorIds


class ThermSensor:
  def __init__(self):
    self.tankSensors = []
    self.mixSensors = []

    for sensor in W1ThermSensor.get_available_sensors():
      if sensor.id in tankSensorIds:
        self.tankSensors.append(sensor)
      elif sensor.id in mixSensorIds:
        self.mixSensors.append(sensor)

  def getMixTemperature(self):
    pass

  def getTankTemperature(self):
    temperatures = [s.get_temperature() for s in self.tankSensors]
    return average(temperatures)

def average(numbers):
  return sum(numbers) / len(numbers)
