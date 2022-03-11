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
    parser.add_argument('--red0', dest="r0", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green0', dest="g0", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue0', dest="b0", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red1', dest="r1", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green1', dest="g1", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue1', dest="b1", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red2', dest="r2", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green2', dest="g2", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue2', dest="b2", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red3', dest="r3", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green3', dest="g3", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue3', dest="b3", action='store', help='set up to 163 color value triplets')
    parser.add_argument('--red4', dest="r4", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green4', dest="g4", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue4', dest="b4", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red5', dest="r5", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green5', dest="g5", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue5', dest="b5", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red6', dest="r6", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green6', dest="g6", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue6', dest="b6", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red7', dest="r7", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green7', dest="g7", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue7', dest="b7", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red8', dest="r8", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green8', dest="g8", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue8', dest="b8", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--red9', dest="r9", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--green9', dest="g9", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--blue9', dest="b9", action='store', help='set up to 16 color value triplets')
    parser.add_argument('--image', dest="img", action='store', help='send a string of 392 characters (a-p), where each character represents a color from the parameter-defined set (a is defined through red1, green1, blue1) on a top left to bottom right matrix.')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    #print('Press Ctrl-C to quit.')
    #if not args.clear:
    #    print('Use "-c" argument to clear LEDs on exit')

    #print('Color wipe animations.')
    colorWipe(strip, Color(127, 127, 127), 1)  # White wipe
    strip.show()
#line 1
    striplen=14
    a = Color(255, 108, 50) if None in (args.r0, args.g0, args.b0) else Color(int(args.r0), int(args.g0), int(args.b0))
    b = Color(132, 127, 127) if None in (args.r1, args.g1, args.b1) else Color(int(args.r1), int(args.g1), int(args.b1))
    c = Color(132, 127, 127) if None in (args.r2, args.g2, args.b2) else Color(int(args.r2), int(args.g2), int(args.b2))
    d = Color(0, 0, 0) if None in (args.r3, args.g3, args.b3) else Color(int(args.r3), int(args.g3), int(args.b3))
    e = Color(255, 215, 0) if None in (args.r4, args.g4, args.b4) else Color(int(args.r4), int(args.g4), int(args.b4))
    f = Color(132, 127, 127) if None in (args.r5, args.g5, args.b5) else Color(int(args.r5), int(args.g5), int(args.b5))
    g = Color(0, 0, 0) if None in (args.r6, args.g6, args.b6) else Color(int(args.r6), int(args.g6), int(args.b6))
    h = Color(0, 0, 0) if None in (args.r7, args.g7, args.b7) else Color(int(args.r7), int(args.g7), int(args.b7))
    i = Color(0, 0, 0) if None in (args.r8, args.g8, args.b8) else Color(int(args.r8), int(args.g8), int(args.b8))
    j = Color(0, 0, 0) if None in (args.r9, args.g9, args.b9) else Color(int(args.r9), int(args.g9), int(args.b9))
    r = len(str(args.img))
    if r == LED_COUNT:
      colorMatrixArray = []
      allowedChars = {"a","b","c","d","e","f","g","h","j"}  # This is the allowed set of characters
      lines = int(r / 28)
      chars = int(r / 14)
      for v in range(lines):
        #print(v)
        colorMatrixArray.append([])
        start = int(v * chars)
        end = start + chars
        line = args.img[start:end]
        #print(line)
        # TODO filter for allowed characters only: a-p
        for w in line:
          # verify that character is in allowed set
          if w in allowedChars: colorMatrixArray[v].append(globals()[w])
          else: colorMatrixArray[v].append(a)
        #print('new dimension')
      print("OK", end='')
    else: 
      colorMatrixArray  = [
        [b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b,b,a,a,a,a,a,a,a,a,a,b,b,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,a,a,a,a,a,a,a,a,a,a,b,a,a,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,a,a,a,a,a,a,a,a,a,b,b,a,a,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,a,a,a,a,a,a,a,a,b,b,b,a,a,a,a,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,a,a,a,a,a,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,a,a,a,a,a,a,b,b,b,a,a,a,a,a,a,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,a,a,a,a,a,a,b,b,a,a,a,a,a,a,a,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,a,a,a,a,b,b,b,a,a,a,a,a,a,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,a,a,a,b,b,b,a,a,a,a,a,a,a,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b,b,a,b,b,a,a,a,a,a,a,b,b,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b,b,b,a,a,a,a,a,a,a,b,b,b,b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b,b,b,b,b,a,a,a,b,b,b,b,b,b,b,b,b,b,b,b,b]
      ]
      print("FALLBACK", end='')
    #print(colorMatrixArray)
    for arr_idx, line in enumerate(colorMatrixArray):
      for lin_idx, val in enumerate(line):
        strip.setPixelColor((striplen * (lin_idx + 1)) - (arr_idx + 1), val)
      strip.show()
