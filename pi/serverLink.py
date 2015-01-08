from requests import get, post
from settings import servername


class ServerLink:

  def getDesiredTemperature(self):
    response = get('%s/desiredTemperature.php' % servername)
    temperature = int(response.text)
    print 'desired temperature is: %d' % temperature
    return temperature

  def postOutputTemp(self, temperature):
    response = post('%s/outputTemperature.php' % servername, data={'temperature': temperature})

  def postTankTemp(self, temperature):
    print 'sending tank temperature to server'
    response = post('%s/tankTemperature.php' % servername, data={'temperature': temperature})
