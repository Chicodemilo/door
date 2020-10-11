#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

print(sys.argv[1])

GPIO.setmode(GPIO.BOARD)
hor = [7, 11, 13, 15]
# vert = [29, 31, 33, 35]

for pin in hor:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


# for pin in pins_two:
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, 0)

fore = [
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
]

aft = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


def turnOne():
    for i in range(260):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(hor[pin], fore[halfstep][pin])
            time.sleep(0.001)


# def openTwo():
#     for i in range(260):
#         for halfstep in range(8):
#             for pin in range(4):
#                 GPIO.output(control_pins[pin], backwards[halfstep][pin])
#             time.sleep(0.001)


turnOne()
# openTwo()

GPIO.cleanup()
