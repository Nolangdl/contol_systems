import time
import board
from analogio import AnalogIn

# Connect an analog sensor to the A1 port of the board you are using. This means a 3V, GND, and signal pin must all be connected.
light = AnalogIn(board.A1)
LED = AnalogOut(board.A0)

# This function turns the analog reading of the sensor (a number from 0 - 65536) to a voltage.
while True:
  light = LED 
