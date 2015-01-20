from requests import get, post
from settings import servername


class ServerLink:

  def getDesiredTemperature(self):
    response = get('http://%s/desiredTemperature' % servername)
    temperature = int(response.text)
    return temperature

  def postOutputTemp(self, temperature):
    response = post('http://%s/outputTemperature' % servername, data={'temperature': temperature})

  def postTankTemp(self, temperature):
    response = post('http://%s/tankTemperature' % servername, data={'temperature': temperature})
