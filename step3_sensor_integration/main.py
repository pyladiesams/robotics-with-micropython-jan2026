from machine import Pin, TouchPad
import neopixel
import time

TOUCH_PIN = 10 # TODO update to the correct pin for the touch sensor

LED_PIN = 48
NUMBER_OF_PIXELS = 1


pixel = neopixel.NeoPixel(Pin(LED_PIN), NUMBER_OF_PIXELS)
touchSensor = TouchPad(Pin(TOUCH_PIN))

blue = (0, 0, 62)
green = (0, 62, 0)
red = (62, 0 , 0)
pink = (62, 0, 31)

TOUCH_THRESHOLD = 30000

def setLEDColor(color):
    pixel[0] = color
    pixel.write()

setLEDColor(blue)

while True:
    touchValue = touchSensor.read()
    if touchValue > TOUCH_THRESHOLD:
        setLEDColor(pink)
    else:
        setLEDColor(blue)
    time.sleep(0.01)

# Make the motor move to the 20° to the left when you touch the pin once and to the right when touching twice.