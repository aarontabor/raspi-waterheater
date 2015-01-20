from RPi.GPIO import setmode, BCM, setup, output, OUT, HIGH, LOW

STATUS_GPIO_PIN = 20

class StatusIndicator:
	def __init__(self):
		setmode(BCM)
		setup(STATUS_GPIO_PIN, OUT, initial=LOW)

	def statusOn(self):
	  output(STATUS_GPIO_PIN, HIGH)

	def statusOff(self):
	  output(STATUS_GPIO_PIN, LOW)
