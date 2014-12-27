from RPi.GPIO import setmode, BCM, setup, output, OUT, HIGH, LOW

ELEMENT_GPIO_PIN = 16


class Element:
  def __init__(self):
    setmode(BCM)
    setup(ELEMENT_GPIO_PIN, OUT, initial=LOW)

  def turnOn(self):
    output(ELEMENT_GPIO_PIN, HIGH)

  def turnOff(self):
    output(ELEMENT_GPIO_PIN, LOW)
