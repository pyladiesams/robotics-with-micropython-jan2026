from machine import Pin
import neopixel
import time

# The pin connected to the LED
LED_PIN = 0 # TODO find out to which ESP pin the onboard RGB LED is connected (it's not 0)


# The neopixel library supports strips or even screens, here we are using a single LED which is just one pixel
NUMBER_OF_PIXELS = 1

# Initialize the LED as a neopixel object
pixel = neopixel.NeoPixel(Pin(LED_PIN), NUMBER_OF_PIXELS)

# colors use RGB values, add your own!
black = (0, 0, 0)
pink = (255, 0, 162)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)


def turnLEDOn():
    pixel[0] = pink
    pixel.write()

def turnLEDOff():
    pixel[0] = black
    pixel.write()
    
while True:
    turnLEDOn()
    time.sleep(0.5)
    turnLEDOff()
    time.sleep(0.5)
