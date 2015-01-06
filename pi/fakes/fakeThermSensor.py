from random import randint

class ThermSensor:
  def __init__(self):
    self.outputTemperature = 75
    self.tankTemperature = 90

  def getOutputTemperature(self):
    self.outputTemperature = step(self.outputTemperature)
    print 'current output temperature: %d' % self.outputTemperature
    return self.outputTemperature


  def getTankTemperature(self):
    self.tankTemperature = step(self.tankTemperature)
    print 'current tank temperature: %d' % self.tankTemperature
    return self.tankTemperature


def step(temperature):
  stepSize = randint(-5,5)
  return temperature + stepSize
  
