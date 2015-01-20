#!/usr/bin/python

from element import Element
from serverLink import ServerLink
from thermSensor import ThermSensor
from settings import heartbeat_seconds
from time import sleep
from statusIndicator import StatusIndicator

statusIndicator = StatusIndicator()
serverLink = ServerLink()
thermSensor = ThermSensor()
element = Element()

statusIndicator.statusOn()

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

  sleep(heartbeat_seconds)

