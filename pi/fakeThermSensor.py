from random import randint

class ThermSensor:
  def __init__(self):
    self.mixTemperature = 75
    self.tankTemperature = 90

  def getMixTemperature(self):
    self.mixTemperature = step(self.mixTemperature)
    print 'current mix temperature: %d' % self.mixTemperature
    return self.mixTemperature


  def getTankTemperature(self):
    self.tankTemperature = step(self.tankTemperature)
    print 'current tank temperature: %d' % self.tankTemperature
    return self.tankTemperature


def step(temperature):
  stepSize = randint(-5,5)
  return temperature + stepSize
  
