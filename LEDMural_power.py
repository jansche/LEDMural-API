#!/usr/bin/env python3
# Simple relay control
# Author: Jan Schenk (jan.schenk@lichtsucht.de)
#

import time
import RPi.GPIO as GPIO
import argparse

RELAY_CONTROL_PIN = 16

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_CONTROL_PIN, GPIO.OUT)

if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-1', '--poweron', dest="power", action='store_true', help='Switch on power on the strip.')
    parser.add_argument('-0', '--poweroff', dest="power", action='store_false', help='Switch off power on the strip.')
    args = parser.parse_args()

    if args.power:
        print("ON", end = '')
        #GPIO.cleanup()
        GPIO.output(RELAY_CONTROL_PIN, True)
    if not args.power:
        print("OFF", end = '')
        GPIO.output(RELAY_CONTROL_PIN, False)
        GPIO.cleanup()
        
# time.sleep(1)

# GPIO.cleanup()

