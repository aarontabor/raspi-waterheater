from serverLink import ServerLink
from random import randint
from time import sleep


heartbeat = 60

def main():
  serverLink = ServerLink()
  tankTemperature = randint(50, 100)
  while True:
    tankTemperature, outputTemperature = nextTemperatures(tankTemperature)
    serverLink.postTankTemp(tankTemperature)
    serverLink.postOutputTemp(outputTemperature)
    sleep(heartbeat)

def nextTemperatures(tankTemperature):
  nextTankTemperature = tankTemperature + randint(-5, 5)
  nextOutputTemperature = nextTankTemperature + randint(-10, 0)
  return (nextTankTemperature, nextOutputTemperature)


if __name__ == '__main__':
  main()
