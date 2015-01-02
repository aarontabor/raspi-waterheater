from element import Element
from time import sleep


def main():
  element = Element()
  while True:
    element.turnOn()
    snooze()
    element.turnOff()
    snooze()

def snooze():
  sleep(2)


if __name__ == '__main__':
  main()
  
