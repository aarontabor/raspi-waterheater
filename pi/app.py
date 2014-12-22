#!/usr/bin/python

from fakeElement import Element
from fakeServerLink import ServerLink
from fakeThermSensor import ThermSensor
from time import sleep

UPDATE_FREQUENCY_SECONDS = 20

serverLink = ServerLink()
thermSensor = ThermSensor()
element = Element()


while True:
  desiredTemp = serverLink.getDesiredTemperature()
  mixedTemp = thermSensor.getMixTemperature() # rename this
  tankTemp = thermSensor.getTankTemperature()

  if tankTemp < desiredTemp:
    element.turnOn()
  else:
    element.turnOff()

  serverLink.postMixedTemp(mixedTemp)
  serverLink.postTankTemp(tankTemp)

  sleep(UPDATE_FREQUENCY_SECONDS)

