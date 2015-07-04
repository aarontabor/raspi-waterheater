from requests import get, post
from settings import servername


class ServerLink:

  def getDesiredTemperature(self):
    response = get('http://%s/desiredTemperature.php' % servername)
    temperature = int(response.text)
    return temperature

  def postOutputTemp(self, temperature):
    response = post('http://%s/outputTemperature.php' % servername, data={'temperature': temperature})
    print(response)

  def postTankTemp(self, temperature):
    response = post('http://%s/tankTemperature.php' % servername, data={'temperature': temperature})
    print(response)
