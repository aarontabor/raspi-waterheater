class ServerLink:
  def getDesiredTemperature(self):
    print 'desired temperature is 95'
    return 95

  def postMixedTemp(self, temperature):
    print 'posting current mixed temperature of %d' % temperature

  def postTankTemp(self, temperature):
    print 'posting current tank temperature of %d' % temperature
