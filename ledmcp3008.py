#for use with led Unknown from github search led and mcp3008

# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	
# Initializing LED pin as OUTPUT pin
led_pin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
# Creating a PWM channel at 100Hz frequency
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0) 
# Read MCP3008 data
def analogInput(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
while True:
	output = analogInput(0) # Reading from CH0
	output = interp(output, [0, 1023], [0, 100])
  	pwm.ChangeDutyCycle(output)
  	sleep(0.1)
