#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import math
import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 392        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 25   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        #time.sleep(wait_ms / 1000.0)
    strip.show()
# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('--red1', dest="r1", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--green1', dest="g1", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--blue1', dest="b1", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--red2', dest="r2", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--green2', dest="g2", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--blue2', dest="b2", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--red3', dest="r3", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--green3', dest="g3", action='store', help='set up to 3 color value triplets')
    parser.add_argument('--blue3', dest="b3", action='store', help='set up to 3 color value triplets')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    #print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    print('Color wipe animations.')
    colorWipe(strip, Color(127, 127, 127), 1)  # White wipe
    strip.show()
#line 1
    striplen=14
    a = Color(255, 108, 50) if None in (args.r1, args.g1, args.b1) else Color(int(args.r1), int(args.g1), int(args.b1))
    b = Color(132, 127, 127) if None in (args.r2, args.g2, args.b2) else Color(int(args.r2), int(args.g2), int(args.b2))
    c = Color(0, 0, 0) if None in (args.r3, args.g3, args.b3) else Color(int(args.r3), int(args.g3), int(args.b3))
    #c = Color("red")
    #c = Color(int(args.r1), int(args.g1), int(args.b1))
    print("Type of Color3: ", type(c))

    colorMatrixArray  = [
      [c, b, b, b, b, b, b, b, b, b, b, b, a, a, a, b, b, b, b, b, b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b, b, b, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b, b, a, a, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b, b, a],
      [a, b, b, b, b, b, b, b, b, b, a, a, a, a, a, a, a, b, b, b, b, b, b, b, b, b, b, b],
      [b, b, b, b, b, b, b, b, b, b, b, b, a, a, a, b, b, b, b, b, b, b, b, b, b, b, b, a]
    ]
    for arr_idx, line in enumerate(colorMatrixArray):
      for lin_idx, val in enumerate(line):
        strip.setPixelColor((striplen * (lin_idx + 1)) - (arr_idx + 1), val)
      strip.show()
