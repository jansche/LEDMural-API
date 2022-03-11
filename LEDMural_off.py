#!/usr/bin/env python3
# Simple relay control
# Author: Jan Schenk (jan.schenk@lichtsucht.de)
#

import time
import RPi.GPIO as GPIO
import argparse

RELAY_CONTROL_PIN = 16
#GPIO.cleanup()
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_CONTROL_PIN, GPIO.OUT)

GPIO.output(RELAY_CONTROL_PIN, False)
# time.sleep(1)

GPIO.cleanup()

