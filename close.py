#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
control_pins = [32, 36, 38, 40]
pins_two = [29, 31, 33, 35]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


for pin in pins_two:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

backwards = [
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
]

halfstep_seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


def openOne():
    for i in range(280):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(pins_two[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)


def openTwo():
    for i in range(280):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], backwards[halfstep][pin])
            time.sleep(0.001)


openOne()
openTwo()

rightNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(">>> CLOSE "+rightNow+"\n")

GPIO.cleanup()
