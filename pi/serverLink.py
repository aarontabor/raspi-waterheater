from requests import get, post

prefix = 'http://www.waterheater.com/waterheater'


class ServerLink:

  def getDesiredTemperature(self):
    response = get('%s/desiredTemperature.php' % prefix)
    temperature = int(response.text)
    print 'desired temperature is: %d' % temperature
    return temperature

  def postOutputTemp(self, temperature):
    pass

  def postTankTemp(self, temperature):
    print 'sending tank temperature to server'
    response = post('%s/tankTemperature.php' % prefix, data={'temperature': temperature})
