#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

direction = sys.argv[1]

GPIO.setmode(GPIO.BOARD)
hor = [7, 11, 13, 15]
vert = [12, 16, 18, 22]

for pin in hor:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


for pin in vert:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

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
    for i in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(hor[pin], fore[halfstep][pin])
            time.sleep(0.001)


def turnTwo():
    for i in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(hor[pin], aft[halfstep][pin])
            time.sleep(0.001)


def turnThree():
    for i in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(vert[pin], fore[halfstep][pin])
            time.sleep(0.001)


def turnFour():
    for i in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(vert[pin], aft[halfstep][pin])
            time.sleep(0.001)


if direction == 'LEFT':
    turnOne()

if direction == 'RIGHT':
    turnTwo()

if direction == 'UP':
    turnThree()

if direction == 'DOWN':
    turnThree()

GPIO.cleanup()
