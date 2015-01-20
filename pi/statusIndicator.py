from RPi.GPIO import setmode, BCM, setup, output, OUT, HIGH, LOW

STATUS_GPIO_PIN = 20

setmode(BCM)
setup(ELEMENT_GPIO_PIN, OUT, initial=LOW)

def statusOn():
  output(ELEMENT_GPIO_PIN, HIGH)

def statusOff():
  output(ELEMENT_GPIO_PIN, LOW)
