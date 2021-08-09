#!/usr/bin/python
import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

zed_pin = 14

GPIO.setup(zed_pin, GPIO.OUT)

GPIO.output(zed_pin, 0)
sleep(5)
GPIO.output(zed_pin, 1)

