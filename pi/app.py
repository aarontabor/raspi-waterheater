#!/usr/bin/python

from element import Element
from serverLink import ServerLink
from ThermSensor import ThermSensor
from time import sleep

UPDATE_FREQUENCY_SECONDS = 20

serverLink = ServerLink()
thermSensor = ThermSensor()
element = Element()


while True:
  desiredTemp = serverLink.getDesiredTemperature()
  outputTemp = thermSensor.getOutputTemperature()
  tankTemp = thermSensor.getTankTemperature()

  if tankTemp < desiredTemp:
    element.turnOn()
  else:
    element.turnOff()

  serverLink.postOutputTemp(outputTemp)
  serverLink.postTankTemp(tankTemp)

  sleep(UPDATE_FREQUENCY_SECONDS)

